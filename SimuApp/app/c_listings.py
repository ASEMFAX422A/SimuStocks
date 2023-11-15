# SimuApp/app/stocks/listings.py
from .models import *
from flask import current_app as app
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required

listings = Blueprint("c_listings", __name__)

login_manager = None
