from datetime import datetime, timedelta
import coins

end_date = datetime.today().timestamp()
start_date = (datetime.today() - timedelta(days=365)).timestamp()

coin = coins.CoinClient('stellar')
resp = coin.get_between(start_date, end_date)

raw = coins.RawResponse(resp)
parse = coins.ParseClear(raw.beautify_between())
parse.parse_days(180)
