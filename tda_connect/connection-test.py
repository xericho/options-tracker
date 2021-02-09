from tda import auth, client
import json
from decouple import config
import os

def authenticate():
    token_path = config('TDA_TOKEN_PATH')
    api_key = config('TDA_API_KEY')
    redirect_uri = config('TDA_REDIRECT_URI')
    try:
        c = auth.client_from_token_file(token_path, api_key)
    except FileNotFoundError:
        from selenium import webdriver
        cwd = os.path.abspath(os.getcwd())
        with webdriver.Chrome(executable_path=os.path.join(cwd, "chromedriver")) as driver:
            c = auth.client_from_login_flow(
                driver, api_key, redirect_uri, token_path)
    return c


if __name__ == '__main__':

    c = authenticate()
    r = c.get_price_history('AAPL',
            period_type=client.Client.PriceHistory.PeriodType.YEAR,
            period=client.Client.PriceHistory.Period.TWENTY_YEARS,
            frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
            frequency=client.Client.PriceHistory.Frequency.DAILY)
    assert r.status_code == 200, r.raise_for_status()
    print(json.dumps(r.json(), indent=4))
