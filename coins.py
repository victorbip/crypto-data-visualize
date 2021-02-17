from datetime import datetime

from pycoingecko import CoinGeckoAPI

import config


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
            raise_type_error(
                "Ticker must either be a string or list of strings.")


class RawResponse:
    # Turns CoinClient response object into readable (UNIX -> DATETIME)
    def __init__(self, data):
        self.data = data
        self.response_dict = dict()

    def __iterate(self, ls):
        # Iterate over the array with values [unix, value]
        arr = list()
        for i in ls:
            # Return an array in the same format as the original object.
            arr.append([datetime.fromtimestamp(i[0] / 1000).date(), i[1]])
        return arr

    def beautify_between(self):
        l, data = self.data[0], self.data[1]
        if isinstance(data, dict):
            # Check if data is a list or not, if yes it iterates over the names of the coins
            if l:
                self.response_dict['multiple'] = True
                for c in data:
                    self.response_dict[c] = {}
                    for k in data[c]:
                        # Update dict_key[coin] with k(price, total_volumes, market_caps) with [[datetime, value], etc.]
                        self.response_dict[c].update(
                            {k: self.__iterate(data[c][k])})
            else:
                self.response_dict['multiple'] = False
                for k in data:
                    # Update k(price, total_volumes, market_caps) with [[datetime, value], etc.]
                    self.response_dict.update({k: self.__iterate(data[k])})
        else:
            # Raise type error, data is not a dict.
            raise_type_error("Data must either be of type dict")

        # Return response dict
        return self.response_dict


class ParseClear:
    # Reformat clear/parsed data from RawResponse
    def __init__(self, data: dict):
        self.data = data

    # Interval = amount of days to skip (7 to get weekly data, 30 to get monthly, etc.)
    def parse_days(self, interval: int):
        is_multiple = self.data['multiple']
        del self.data['multiple']
        if is_multiple:
            for c in self.data:
                for k in self.data[c]:
                    self.data[c][k] = self.data[c][k][::interval]

        else:
            for k in self.data:
                self.data[k] = self.data[k][::interval]

        return self.data
