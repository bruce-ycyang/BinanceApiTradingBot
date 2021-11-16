import backtrader as bt


class RSIstrategy(bt.Strategy):
    def __init__(self):
        self.rsi = bt.talib.RSI(self.data, period=14)

    def next(self):
        if self.rsi < 30 and not self.position:
            self.buy(size=1)
        if self.rsi > 70 and self.position:
            self.close()


cerebro = bt.Cerebro()

data = bt.feeds.GenericCSVData(dataname="./data/daily.csv", dtformat=2)

cerebro.adddata(data)
cerebro.addstrategy(RSIstrategy)
cerebro.run()

cerebro.plot()
