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
from flask_login import current_user, login_required
from flask import current_app as app
from .models import User

c_portfolio = Blueprint("c_portfolio", __name__)

login_manager = None


@login_required
@c_portfolio.route("/portfolio")
def portfolio():
    return render_template(
        "pages/user/portfolio.html"
    )
