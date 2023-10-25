import schedule
import time
from get_data import get_stock_price
from save_data import save_data


def create_job(ticker):
    def job():
        price = get_stock_price(ticker)
        save_data(price, ticker)
        print(f"Saved {ticker} stock price: {price}")

    return job


if __name__ == "__main__":
    tickers = ["AAPL", "MSFT", "GOOGL", "EOAN.DE"]

    for ticker in tickers:
        job = create_job(ticker)
        schedule.every(15).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
