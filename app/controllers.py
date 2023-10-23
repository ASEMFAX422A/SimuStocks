from app import app, login_manager


from flask_login import login_user, logout_user, current_user, login_required
from flask import render_template, redirect, url_for


@login_manager.user_loader
def load_user(userid):
    return User.objects(id=userid).first()


@app.route("/produce_debug")
def produce_debug():
    if current_user.is_authenticated:
        app.logger.debug("Debug was produced by %s" % current_user.full_name)
        # current_user.full_name requires we have the function in User model to return full_name
    else:
        app.logger.debug("Debug was produced by Anonymous")
    return redirect(url_for('index'))


@app.route("/produce_info")
def produce_info():
    if current_user.is_authenticated:
        app.logger.info("Info was produced by %s" % current_user.full_name)
        # current_user.full_name requires we have the function in User model to return full_name
    else:
        app.logger.info("Info was produced by Anonymous")
    return redirect(url_for('index'))


@app.route("/produce_warning")
def produce_warning():
    if current_user.is_authenticated:
        app.logger.warning("Warning was produced by %s" % current_user.full_name)
        # current_user.full_name requires we have the function in User model to return full_name
    else:
        app.logger.warning("Warning was produced by Anonymous")
    return redirect(url_for('index'))


@app.route("/produce_error")
def produce_error():
    if current_user.is_authenticated:
        app.logger.error("Error was produced by %s" % current_user.full_name)
        # current_user.full_name requires we have the function in User model to return full_name
    else:
        app.logger.error("Error was produced by Anonymous")
    return redirect(url_for('index'))


@app.route("/produce_critical")
def produce_critical():
    if current_user.is_authenticated:
        app.logger.critical("CRITICAL was produced by %s" % current_user.full_name)
        # current_user.full_name requires we have the function in User model to return full_name
    else:
        app.logger.critical("CRITICAL was produced by Anonymous")
    return redirect(url_for('index'))


@app.route('/')
def index():
    return render_template('index.html')
