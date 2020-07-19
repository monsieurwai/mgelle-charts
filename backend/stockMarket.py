import yfinance as yf


class StockMarket:

    def __init__(self, quote, period, interval):
        self.quote = quote

    def getData(self):
        return self.askToYahooFinance(self.quote, self.period, self.interval)

    def askToYahooFinance(self, quote, period, interval):
        ticker = yf.Ticker(quote)
        data = ticker.history(period=period, interval=interval)
        # TODO --> clean data
        return {}
