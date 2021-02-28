from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from colour import Color
import pandas as pd
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from strategies.models import Order

@login_required
@api_view(['GET'])
def get_option_data(request):
    values = ['transaction_date', 'net_amount', 'total_fees', 'ticker']
    orders = [o for o in Order.objects.filter(user=request.user).values(*values) if o['net_amount']]
    df = pd.DataFrame(orders)
    df['day'] = df.transaction_date.apply(lambda x: x.day)
    df['month'] = df.transaction_date.apply(lambda x: x.month)
    df['year'] = df.transaction_date.apply(lambda x: x.year)
    df['net_amount'] = df.net_amount.astype(float)

    # Group dates to get unique dates
    df_dates = df.groupby([df.day, df.month, df.year], as_index=False).sum()
    df_dates['date'] = df_dates.apply(lambda x: datetime(int(x.year), int(x.month), int(x.day)).strftime('%Y-%m-%d'), axis=1)
    df_dates = df_dates.sort_values(by='date')
    df_dates.net_amount = df_dates.net_amount.cumsum().round(2)
    today = datetime.today()

    perf_all = [{
        'date': x.date,
        'profit': x.net_amount,
    } for i, x in df_dates.iterrows()]

    df_ytd = df_dates[df_dates.year == today.year]
    perf_ytd = [{
        'date': x.date,
        'profit': x.net_amount,
    } for i, x in df_ytd.iterrows()]

    df_month = df_dates[df_dates.month == today.month]
    perf_month = [{
        'date': x.date,
        'profit': x.net_amount,
    } for i, x in df_month.iterrows()]

    # Ticker performance
    df_ticker = df.groupby([df.ticker], as_index=False).sum()
    df_ticker = df_ticker.sort_values(by='net_amount', ascending=False)
    df_gainers = df_ticker[df_ticker.net_amount >= 0]
    # red = Color("green")
    # darkred = Color("red")
    # df_gainers['color'] = [c.hex for c in red.range_to(darkred, df_gainers.shape[0])]
    perf_gainers_ticker = [{
        'ticker': x.ticker,
        'profit': x.net_amount,
        'color': "#46c35f"
    } for i, x in df_gainers.iterrows()]

    df_losers = df_ticker[df_ticker.net_amount < 0]
    # df_losers['color'] = [c.hex for c in red.range_to(darkred, df_losers.shape[0])]
    perf_losers_ticker = [{
        'ticker': x.ticker,
        'profit': x.net_amount,
        'color': "maroon"
    } for i, x in df_losers.iterrows()]

    return Response({
        'perf_all': perf_all,
        'perf_ytd': perf_ytd,
        'perf_month': perf_month,
        'perf_gainers_ticker': perf_gainers_ticker,
        'perf_losers_ticker': perf_losers_ticker,
    })

@login_required
def home(request):
    return render(request, "frontend/home.html", {})
