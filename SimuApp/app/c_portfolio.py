# SimuApp/app/c_portfolio.py
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

c_portfolio = Blueprint("c_portfolio", __name__)

login_manager = None


@c_portfolio.route("/portfolio")
def portfolio():
    return render_template("pages/user/portfolio.html")
