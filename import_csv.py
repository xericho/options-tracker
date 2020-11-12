import pandas as pd
from dateutil.parser import parse
from django.contrib.auth import get_user_model

from strategies.models import *


def load_basic_options():
    """
    from import_csv import load_basic_options; load_basic_options()
    """
    df = pd.read_csv('./basic_options.csv')
    df = df.where(pd.notnull(df), None)
    td_broker = Broker.objects.get(pk=13)
    rh_broker = Broker.objects.get(pk=14)
    for index, row in df.iterrows():
        broker = td_broker if row['Account'] == 'TD Ameritrade' else rh_broker
        close_date = parse(row['Close Date']).strftime('%Y-%m-%d') if row['Close Date'] else None
        close_price = row['Exit Price'] if row['Exit Price'] else None
        pl = float(row['P/L'].replace('$','').replace(',','')) if row['P/L'] else None
        BasicOption.objects.create(
            ticker=row['Stock Symbol'],
            open_date=parse(row['Open Date']).strftime('%Y-%m-%d'),
            close_date=close_date,
            exp_date=parse(row['Exp Date']).strftime('%Y-%m-%d'),
            longshort=row['Long or Short'].lower(),
            callput=row['Call or Put'].lower(),
            strike=row['Strike Price'],
            premium=row['Premium'],
            quantity=row['#'],
            stock_price=row['Stock Price'],
            fees=row['Fees'],
            close_price=close_price,
            broker=broker,
            status=row['Details'].lower(),
            profitloss=pl,
            user=get_user_model().objects.get(username='ho')
        )


def load_spread_options():
    """
    from import_csv import load_spread_options; load_spread_options()
    """
    df = pd.read_csv('./spread_options.csv')
    df = df.where(pd.notnull(df), None)
    td_broker = Broker.objects.get(pk=13)
    rh_broker = Broker.objects.get(pk=14)
    for i in range(0, df.shape[0], 2):
        # Get every 2 rows
        row = df.iloc[i:i+2,:]
        broker = td_broker if row.iloc[0]['Account'] == 'TD Ameritrade' else rh_broker
        close_date = parse(row.iloc[0]['Close Date']).strftime('%Y-%m-%d') if row.iloc[0]['Close Date'] else None
        close_price = row.iloc[0]['Exit Price'] if row.iloc[0]['Exit Price'] else None
        pl = float(row.iloc[0]['P/L'].replace('$','').replace(',','')) if row.iloc[0]['P/L'] else None
        SpreadOption.objects.create(
            ticker=row.iloc[0]['Stock Symbol'],
            open_date=parse(row.iloc[0]['Open Date']).strftime('%Y-%m-%d'),
            close_date=close_date,
            exp_date=parse(row.iloc[0]['Exp Date']).strftime('%Y-%m-%d'),
            creditdebit=row.iloc[0]['Debit or Credit'].lower(),
            callput=row.iloc[0]['Call or Put'].lower(),
            strike1=row.iloc[0]['Strike Price'],
            strike2=row.iloc[1]['Strike Price'],
            premium=row.iloc[0]['Net Premium'],
            quantity=row.iloc[0]['#'],
            stock_price=row.iloc[0]['Stock Price'],
            fees=row.iloc[0]['Fees'],
            close_price=close_price,
            broker=broker,
            status=row.iloc[0]['Details'].lower(),
            profitloss=pl,
            user=get_user_model().objects.get(username='ho')
        )
