from datetime import datetime
import config
from pycoingecko import CoinGeckoAPI


class CoinClient:

    def __init__(self, ticker):
        self.ticker = ticker
        self.cg = CoinGeckoAPI()

    def get_between(self, start_date: float, end_date: float):
        if isinstance(self.ticker, str):
            return True, self.cg.get_coin_market_chart_range_by_id(self.ticker, config.currency, start_date, end_date)
        elif isinstance(self.ticker, list):
            pass
        else:
            return False, "Ticker is not an instance of str or list."
