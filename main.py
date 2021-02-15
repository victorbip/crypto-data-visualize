import pandas
import matplotlib
from datetime import datetime, timedelta
import coins as coin

start_date = datetime(2017,6,1)
end_date = datetime(2018,6,1)
client = coin.CoinClient("bitcoin")
print(client.get_between(start_date, end_date))