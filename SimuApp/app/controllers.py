# SimuApp/app/controllers.py
from flask import current_app as app
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required

main = Blueprint("main", __name__)

login_manager = None  # Initialisieren Sie login_manager als None

from .models import *


def init_app(lm):
    global login_manager
    login_manager = lm

    # Verschieben Sie den user_loader Dekorator in die init_app Funktion
    @login_manager.user_loader
    def load_user(userid):
        return User.objects(id=userid).first()


@main.route("/produce_debug")
def produce_debug():
    if current_user.is_authenticated:
        app.logger.debug("Debug was produced by %s" % current_user.full_name)
        # current_user.full_name requires we have the function in User model to return full_name
    else:
        app.logger.debug("Debug was produced by Anonymous")
    return redirect(url_for("main.index"))


@main.route("/produce_info")
def produce_info():
    if current_user.is_authenticated:
        app.logger.info("Info was produced by %s" % current_user.full_name)
        # current_user.full_name requires we have the function in User model to return full_name
    else:
        app.logger.info("Info was produced by Anonymous")
    return redirect(url_for("main.index"))


@main.route("/produce_warning")
def produce_warning():
    if current_user.is_authenticated:
        app.logger.warning("Warning was produced by %s" % current_user.full_name)
        # current_user.full_name requires we have the function in User model to return full_name
    else:
        app.logger.warning("Warning was produced by Anonymous")
    return redirect(url_for("main.index"))


@main.route("/produce_error")
def produce_error():
    if current_user.is_authenticated:
        app.logger.error("Error was produced by %s" % current_user.full_name)
        # current_user.full_name requires we have the function in User model to return full_name
    else:
        app.logger.error("Error was produced by Anonymous")
    return redirect(url_for("main.index"))


@main.route("/produce_critical")
def produce_critical():
    if current_user.is_authenticated:
        app.logger.critical("CRITICAL was produced by %s" % current_user.full_name)
        # current_user.full_name requires we have the function in User model to return full_name
    else:
        app.logger.critical("CRITICAL was produced by Anonymous")
    return redirect(url_for("main.index"))


@main.route("/")
def index():
    return render_template("index.html")


@main.errorhandler(401)
def http_error_unauthorized(e):
    return render_template("errors/error.html"), 401


@main.errorhandler(403)
def http_error_forbidden(e):
    return render_template("errors/error.html"), 403


@main.errorhandler(404)
def http_error_page_not_found(e):
    if current_user.is_authenticated:
        app.logger.info(
            "%s tryed to Request %s but this doesn't exist"
            % (current_user, request.path)
        )
    else:
        app.logger.info(
            "unknown User tryed to Request %s but this doesn't exist" % request.endpoint
        )
    return render_template("errors/error.html"), 404


@main.errorhandler(500)
def http_error_internal_server_error(e):
    return render_template("errors/error.html"), 500


@main.errorhandler(Exception)
def handle_exception(e):
    if current_user.is_authenticated:
        app.logger.error("%s created UNEXPEDTED ERROR: %s" % (current_user, e))
    else:
        app.logger.error("unknown User created UNEXPEDTED ERROR: %s" % e)
    return http_error_internal_server_error(e)
