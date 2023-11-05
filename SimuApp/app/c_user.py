# SimuApp/app/c_user.py
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

c_user = Blueprint("c_user", __name__)

login_manager = None
