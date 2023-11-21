# SimuApp/app/c_listings.py
from .models import Stocks
from flask import current_app as app
from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    session,
    abort,
    flash,
)

c_listings = Blueprint("c_listings", __name__)

login_manager = None

prices_list = []
timestamp_list = []


@c_listings.route("/stocks/listings/")
def listings():
    stocks = Stocks.objects()
    return render_template("pages/stocks/listings.html", stocks=stocks)


@c_listings.route("/stocks/ticker/<ticker_name>")
def listings_ticker(ticker_name):
    ticker = Stocks.objects(ticker=ticker_name).first_or_404()

    if ticker:
        for data_point in ticker.data:
            prices_list.append(data_point['price'])
            timestamp_list.append(data_point['timestamp'])

    return render_template("pages/stocks/ticker.html", ticker=ticker, prices_list=prices_list, timestamp_list=timestamp_list)
