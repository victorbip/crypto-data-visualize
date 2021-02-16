from datetime import datetime
import config
from pycoingecko import CoinGeckoAPI


def raise_type_error(message):
    # Raises a type error
    raise TypeError(message)


class CoinClient:
    # Response object keys (per coin)
    # prices
    # market_caps
    # total_volumes

    def __init__(self, ticker):
        self.ticker = ticker
        self.cg = CoinGeckoAPI()
        self.response_dict = dict()

    # Gets raw data between start and end date (UNIX time format)
    def get_between(self, start_date: float, end_date: float):
        # Returns one CoinGecko response object for coin specified
        if isinstance(self.ticker, str):
            return False, self.cg.get_coin_market_chart_range_by_id(self.ticker, config.currency, start_date, end_date)

        # Returns a dict of CoinGecko response objects for coins specified
        elif isinstance(self.ticker, list):
            for c in self.ticker:
                self.response_dict[c] = self.cg.get_coin_market_chart_range_by_id(c, config.currency, start_date,
                                                                                  end_date)

            return True, self.response_dict
        # Raise TypeError is self.ticker isn't a string or list.
        else:
            raise_type_error("Ticker must either be a string or list of strings.")


class RawResponse:
    # Turns CoinClient response object into readable (UNIX -> DATETIME)
    def __init__(self, data):
        self.data = data
        self.response_dict = dict()

    def iterate(self, ls):
        arr = list()
        for i in ls:
            arr.append([datetime.fromtimestamp(i[0] / 1000).date(), i[1]])
        return arr

    def beautify_between(self):
        l, data = self.data[0], self.data[1]
        if isinstance(data, dict):
            # Check if data is a list or not, if yes it iterates over the names of the coins
            if l:
                for c in data:
                    self.response_dict[c] = {}
                    for k in data[c]:
                        self.response_dict[c].update({k: self.iterate(data[c][k])})
            else:
                for k in data:
                    self.response_dict.update({k: self.iterate(data[k])})
        else:
            raise_type_error("Data must either be of type dict")
        return self.response_dict
