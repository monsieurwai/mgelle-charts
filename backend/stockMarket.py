import yfinance as yf
import pandas as pd

class StockMarket:

    def __init__(self, quote, period, interval):
        self.quote = quote
        self.period = period
        self.interval = interval

    def getData(self):
        return self.askToYahooFinance(self.quote, self.period, self.interval)

    def askToYahooFinance(self, quote, period, interval):
        ticker = yf.Ticker(quote)
        stockDataBrut = ticker.history(period=period, interval=interval)
        stockData = self.cleanData(stockDataBrut)
        return stockData

    def cleanData(self, data):
        cleanData = data.to_json(orient='table')
        return cleanData
