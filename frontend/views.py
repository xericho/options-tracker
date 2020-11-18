from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from colour import Color
import pandas as pd
from datetime import datetime

from strategies.models import BasicOption, SpreadOption

@login_required
def home(request):
    values = ['open_date', 'profitloss', 'fees', 'ticker']
    basics = [o for o in BasicOption.objects.values(*values) if o['profitloss']]
    spreads = [o for o in SpreadOption.objects.values(*values) if o['profitloss']]
    df = pd.DataFrame(basics + spreads)
    df['day'] = df.open_date.apply(lambda x: x.day)
    df['month'] = df.open_date.apply(lambda x: x.month)
    df['year'] = df.open_date.apply(lambda x: x.year)
    df['profitloss'] = df.profitloss.astype(float) - df.fees.astype(float)

    # Group dates to get unique dates
    df_dates = df.groupby([df.day, df.month, df.year], as_index=False).sum()
    df_dates['date'] = df_dates.apply(lambda x: datetime(int(x.year), int(x.month), int(x.day)).strftime('%Y-%m-%d'), axis=1)
    df_dates = df_dates.sort_values(by='date')

    df_all = df_dates.groupby([df_dates.month, df_dates.year], as_index=False).sum()
    df_all['date'] = df_all.apply(lambda x: datetime(int(x.year), int(x.month), 1).strftime('%Y-%m-%d'), axis=1)
    df_all['profitloss'] = df_all.profitloss.round(2)
    perf_all = [{
        'date': x.date,
        'profit': x.profitloss,
    } for i, x in df_all.iterrows()]

    df_dates.profitloss = df_dates.profitloss.cumsum().round(2)
    today = datetime.today()
    df_ytd = df_dates[df_dates.year == today.year]
    perf_ytd = [{
        'date': x.date,
        'profit': x.profitloss,
    } for i, x in df_ytd.iterrows()]

    df_month = df_dates[df_dates.month == today.month]
    perf_month = [{
        'date': x.date,
        'profit': x.profitloss,
    } for i, x in df_month.iterrows()]

    # Ticker performance
    df_ticker = df.groupby([df.ticker], as_index=False).sum()
    df_ticker = df_ticker.sort_values(by='profitloss', ascending=False)
    df_gainers = df_ticker[df_ticker.profitloss >= 0]
    # red = Color("green")
    # darkred = Color("red")
    # df_gainers['color'] = [c.hex for c in red.range_to(darkred, df_gainers.shape[0])]
    perf_gainers_ticker = [{
        'ticker': x.ticker,
        'profit': x.profitloss,
        'color': "#46c35f"
    } for i, x in df_gainers.iterrows()]

    df_losers = df_ticker[df_ticker.profitloss < 0]
    # df_losers['color'] = [c.hex for c in red.range_to(darkred, df_losers.shape[0])]
    perf_losers_ticker = [{
        'ticker': x.ticker,
        'profit': x.profitloss,
        'color': "maroon"
    } for i, x in df_losers.iterrows()]

    return render(request, "frontend/home.html", {
        'perf_all': perf_all,
        'perf_ytd': perf_ytd,
        'perf_month': perf_month,
        'perf_gainers_ticker': perf_gainers_ticker,
        'perf_losers_ticker': perf_losers_ticker,
    })
