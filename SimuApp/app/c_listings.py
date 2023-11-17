# SimuApp/app/c_listings.py
from .models import *
from . import db
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


@c_listings.route("/stocks/listings")
def listings():
    return render_template("pages/stocks/listings.html")
