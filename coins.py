from datetime import datetime
import config
from pycoingecko import CoinGeckoAPI


def raise_type_error(message):
    raise TypeError(message)


class CoinClient:
    def __init__(self, ticker):
        self.ticker = ticker
        self.cg = CoinGeckoAPI()
        self.response_dict = dict()

    # Gets raw data between start and end date (UNIX time format)
    def get_between(self, start_date: float, end_date: float):
        # Returns one CoinGecko response object for coin specified
        if isinstance(self.ticker, str):
            return self.cg.get_coin_market_chart_range_by_id(self.ticker, config.currency, start_date, end_date)
        # Returns a dict of CoinGecko response objects for coins specified
        elif isinstance(self.ticker, list):
            for c in self.ticker:
                self.response_dict[c] = self.cg.get_coin_market_chart_range_by_id(c, config.currency, start_date, end_date)
            return self.response_dict
        # Raise TypeError is self.ticker isn't a string or list.
        else:
            raise_type_error("Ticker must either be a string or list of strings.")


class RawResponse:
    def __init__(self, data):
        self.data = data

    def beautify(self):
        if isinstance(self.data, dict):
            pass
        elif isinstance(self.data, list):
            pass
        else:
            raise_type_error("Data must either be a dict or a list of dicts")
