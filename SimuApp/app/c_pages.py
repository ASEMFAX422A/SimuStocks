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
