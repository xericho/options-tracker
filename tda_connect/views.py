import pandas as pd
from dateparser import parse
from tda.client import Client
from tda.auth import easy_client, client_from_login_flow, client_from_token_file
from decouple import config
from datetime import datetime
import json
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import status

from brokerage.models import Broker
from strategies.models import Order, STATUS


def authenticate():
    """
    Authenticates user using easy client
    """
    token_path = config('TDA_TOKEN_PATH')
    api_key = config('TDA_API_KEY')
    redirect_uri = config('TDA_REDIRECT_URI')
    try:
        c = client_from_token_file(token_path, api_key)
    except FileNotFoundError:
        from selenium import webdriver
        cwd = os.path.abspath(os.getcwd())
        with webdriver.Chrome(executable_path=os.path.join(cwd, "chromedriver")) as driver:
            c = client_from_login_flow(
                driver, api_key, redirect_uri, token_path)
    return c


class SyncBroker(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def checkStatusCode(self, r):
        if r.status_code != 200:
            print(r.text)
            raise Exception(f'Error: {r.text}')

    def process(self, transactions, broker):
        """
        Saves the data to relevent strategy tables
        """
        # Only option trades are of type 'TRADE' and 'RECEIVE_AND_DELIVER' and of asset type 'OPTION'
        transactions = [t for t in transactions if t['type'] in ['TRADE', 'RECEIVE_AND_DELIVER']
                        and t['transactionItem']['instrument']['assetType'] == 'OPTION'
                        and t['transactionSubType'] != 'IT']
        df = pd.DataFrame(transactions)
        df['totalFees'] = df.fees.apply(lambda x: sum(x.values()))
        df['cusip'] = df.transactionItem.apply(lambda x: x['instrument']['cusip'])
        df['transactionDate'] = df.transactionDate.apply(lambda x: parse(x))
        df['expDate'] = df.transactionItem.apply(lambda x: parse(x['instrument']['optionExpirationDate']))
        df['ticker'] = df.cusip.apply(lambda x: x.split('.')[0][1:])

        with open('tda_transactions.json', 'w') as f:
            json.dump(transactions, f, indent=4)

        for idx, row in df.iterrows():
            Order.objects.create(
                cusip = row.cusip,
                ticker = row.ticker,
                transaction_date = row.transactionDate,
                exp_date = row.expDate,
                longshort = row.transactionItem.get('instruction', None),
                callput = row.transactionItem.get('instruction', None),
                status = row.transactionItem.get('positionEffect', 'expired'),
                quantity = row.transactionItem.get('amount', 'expired'),
                net_amount = row.netAmount,
                total_fees = row.totalFees,
                broker = broker,
                user = self.request.user,
            )


    def fetchOpenPositions(self, c, broker):
        r = c.get_account(broker.account_id, fields=Client.Account.Fields.POSITIONS)
        self.checkStatusCode(r)
        with open('tda_positions.json', 'w') as f:
            json.dump(r.json(), f, indent=4)
        return r.json()


    def fetchAllTransactions(self, c, broker):
        r = c.get_transactions(
            broker.account_id,
            transaction_type=Client.Transactions.TransactionType.ALL,
            start_date=broker.last_synced,
        )
        self.checkStatusCode(r)
        return r.json()

    def get(self, request, format=None):
        broker_id = request.GET.get('id')

        try:
            broker = Broker.objects.get(user=request.user, id=broker_id, broker='TD')
        except Exception as e:
            print('Error: Invalid brokerage')
            return Response('Invalid brokerage', status=status.HTTP_400_BAD_REQUEST)

        c = authenticate()
        # positions = self.fetchOpenPositions(c, broker)
        transactions = self.fetchAllTransactions(c, broker)

        self.process(transactions, broker)

        return Response('Success!')

