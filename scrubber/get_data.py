import yfinance as yf


def get_stock_price(ticker):
    stock_info = yf.Ticker(ticker)
    todays_data = stock_info.history(period="1d")
    return todays_data["Close"][0]
