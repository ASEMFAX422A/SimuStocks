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
        # Plan the job to run once a day at a specific time
        schedule.every().day.at("21:47").do(job)

    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(1)
