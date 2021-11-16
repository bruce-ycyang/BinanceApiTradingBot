import csv
import config
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET)

candles = client.get_klines(symbol="BNBBTC", interval=Client.KLINE_INTERVAL_30MINUTE)

csvfile = open("oneday.csv", "w", newline="")
candlestick_writer = csv.writer(csvfile, delimiter=",")

# for candle in candles:
#     print(candle)

#     candlestick_writer.writerow(candle)

# print(len(candles))

candlestikers = client.get_historical_klines(
    "BNBUSDT", Client.KLINE_INTERVAL_1DAY, "1 Dec, 2018", "1 Jan, 2020"
)
for candlestiker in candlestikers:
    candlestiker[0] = candlestiker[0] / 1000
    candlestick_writer.writerow(candlestiker)

csvfile.close()
