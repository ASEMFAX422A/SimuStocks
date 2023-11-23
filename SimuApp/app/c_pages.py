# SimuApp/app/c_pages.py
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

c_pages = Blueprint("c_pages", __name__)

login_manager = None


@c_pages.route("/faq")
def faq():
    return render_template("pages/faq.html")


@c_pages.route("/user/profile")
def profile():
    return render_template("pages/user/profile.html")


@c_pages.route("/contact")
def contact():
    return render_template("pages/contact.html")
