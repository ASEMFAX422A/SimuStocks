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


@c_listings.route("/stocks/listings/")
def listings():
    stocks = Stocks.objects()
    return render_template("pages/stocks/listings.html", stocks=stocks)


@c_listings.route("/stocks/listings/<ticker_name>")
def listings_ticker(ticker_name):
    ticker = Stocks.objects(ticker=ticker_name).first_or_404()
    return render_template("pages/stocks/listings.html", ticker=ticker)
