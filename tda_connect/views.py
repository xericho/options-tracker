from tda.client import Client
from tda.auth import easy_client
from decouple import config
from datetime import datetime
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import status

from brokerage.models import Broker


def authenticate():
    """
    Authenticates user using easy client
    """
    c = easy_client(
        token_path=config('TDA_TOKEN_PATH'),
        api_key=config('TDA_API_KEY'),
        redirect_uri=config('TDA_REDIRECT_URI'),
    )
    return c


class SyncBroker(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        broker_id = request.GET.get('id')

        try:
            broker = Broker.objects.get(user=request.user, id=broker_id, broker='TD')
        except Exception as e:
            print('Error: Invalid brokerage')
            return Response('Invalid brokerage', status=status.HTTP_400_BAD_REQUEST)

        c = authenticate()
        # r = c.get_account(broker.account_id, fields=Client.Account.Fields.ORDERS)
        r = c.get_transactions(
            broker.account_id,
            transaction_type=Client.Transactions.TransactionType.ALL,
            start_date=broker.last_synced,
        )
        data = [t for t in r.json() if t['type'] in ['TRADE', 'RECEIVE_AND_DELIVER']]


        if r.status_code != 200:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        with open('tda_transactions.json', 'w') as f:
            json.dump(data, f, indent=4)

        return Response(data)

