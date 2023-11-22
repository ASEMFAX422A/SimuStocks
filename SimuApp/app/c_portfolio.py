# SimuApp/app/c_portfolio.py
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
from flask import current_app as app
from .models import User

c_portfolio = Blueprint("c_portfolio", __name__)

login_manager = None


@c_portfolio.route("/portfolio")
def portfolio():
    current_user = User.objects
    return render_template("pages/user/portfolio.html", current_user_full_name=current_user)
