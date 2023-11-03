# SimuApp/app/stocks/listings.py
from .models import *
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

listings = Blueprint("c_listings", __name__)

login_manager = None


@listings.route("/stocks/listings")
def listings():
    return render_template("stocks/listings.html")
