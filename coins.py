from datetime import datetime
import config
import requests


class CoinClient:
    cmc_endpoint = "https://pro-api.coinmarketcap.com/v1/cryptocurrency"

    def __init__(self, ticker):
        self.ticker = ticker
        self.api_header = {"X-CMC_PRO_API_KEY": config.cmc_api}

    def fetch_historical(self, s, e):
        data = {}
        response = requests.get(f"{self.cmc_endpoint}/listings/historical", headers=self.api_header).json()

    def get_between(self, start_date: datetime, end_date: datetime):
        if isinstance(self.ticker, str):
            return True,
        elif isinstance(self.ticker, list):
            return True,
        else:
            return False, "Ticker is not an instance of str or list."
