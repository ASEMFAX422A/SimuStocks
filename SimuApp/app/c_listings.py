# SimuApp/app/c_listings.py
from .models import Stocks
from flask import (
    Blueprint,
    current_app as app,
    render_template,
    abort,
)

c_listings = Blueprint("c_listings", __name__)
login_manager = None  


def format_price(price):
    return f"Formatierter Preis: {price}"

def format_timestamp(timestamp):
    return f"Formatierter Timestamp: {timestamp}"

app.jinja_env.filters['format_price'] = format_price
app.jinja_env.filters['format_timestamp'] = format_timestamp

@c_listings.route("/stocks/listings/")
def listings():
    stocks = Stocks.objects()
    return render_template("pages/stocks/listings.html", stocks=stocks)

@c_listings.route("/stocks/ticker/<ticker_name>")
def listings_ticker(ticker_name):
    prices_list = []
    timestamp_list = []
    ticker = Stocks.objects(ticker=ticker_name).first_or_404()

    if ticker:
        for data_point in ticker.data:
            prices_list.append(data_point["price"])
            timestamp_list.append(data_point["timestamp"])

    return render_template(
        "pages/stocks/ticker.html",
        ticker=ticker,
        prices_list=prices_list,
        timestamp_list=timestamp_list,
    )