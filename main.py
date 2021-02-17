from datetime import datetime, timedelta

import coins
import plot

end_date = datetime.today().timestamp()
start_date = (datetime.today() - timedelta(days=365)).timestamp()

coin = coins.CoinClient('cardano')
resp = coin.get_between(start_date, end_date)

raw = coins.RawResponse(resp)
parse = coins.ParseClear(raw.beautify_between())

response = plot.sanitize_response(parse.parse_days(30), "prices", False)
plotarr = plot.PlotArray(response['x_axis'], response['y_axis'])
plotarr.line_graph_price("Cardano", False)
