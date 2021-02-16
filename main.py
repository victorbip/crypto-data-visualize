from datetime import datetime, timedelta
import coins as coin

end_date = datetime.today().timestamp()
start_date = (datetime.today() - timedelta(days=365)).timestamp()
coin = coin.CoinClient("cardano")
print(coin.get_between(start_date, end_date))
