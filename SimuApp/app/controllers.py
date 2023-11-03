# SimuApp/app/controllers.py
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
from flask_login import login_user, logout_user, current_user, login_required

from flask_principal import identity_changed, Identity, AnonymousIdentity

from .forms import LoginForm, RegisterForm
from .utils import safe_cast, is_valid_object_id, is_safe_url

main = Blueprint("main", __name__)

login_manager = None  # Initialisieren Sie login_manager als None


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
        # current_user.full_name requires
        # that we have the function in User model to return full_name
    else:
        app.logger.debug("Debug was produced by Anonymous")
    return redirect(url_for("main.index"))


@main.route("/produce_info")
def produce_info():
    if current_user.is_authenticated:
        app.logger.info("Info was produced by %s" % current_user.full_name)
        # current_user.full_name requires
        # that we have the function in User model to return full_name
    else:
        app.logger.info("Info was produced by Anonymous")
    return redirect(url_for("main.index"))


@main.route("/produce_warning")
def produce_warning():
    if current_user.is_authenticated:
        app.logger.warning("Warning was produced by %s" %
                           current_user.full_name)
        # current_user.full_name requires
        # that we have the function in User model to return full_name
    else:
        app.logger.warning("Warning was produced by Anonymous")
    return redirect(url_for("main.index"))


@main.route("/produce_error")
def produce_error():
    if current_user.is_authenticated:
        app.logger.error("Error was produced by %s" % current_user.full_name)
        # current_user.full_name requires
        # that we have the function in User model to return full_name
    else:
        app.logger.error("Error was produced by Anonymous")
    return redirect(url_for("main.index"))


@main.route("/produce_critical")
def produce_critical():
    if current_user.is_authenticated:
        app.logger.critical("CRITICAL was produced by %s" %
                            current_user.full_name)
        # current_user.full_name requires that
        # we have the function in User model to return full_name
    else:
        app.logger.critical("CRITICAL was produced by Anonymous")
    return redirect(url_for("main.index"))


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/login", methods=["GET", "POST"])
def login():
    session["redirect_next"] = request.args.get(
        "next", session.get("redirect_next"))
    if not is_safe_url(session["redirect_next"]):
        return abort(400)
    if request.method == "GET":
        form = LoginForm()
        return render_template("accounting/login.html", form=form)
    if request.method == "POST":
        form = LoginForm(request.form)
        user_email = str(form.email.data).lower()
        user = User.objects(email=user_email).first()

        if not user:
            rform = RegisterForm(email=user_email)

            flash(
                "Deine E-Mail wurde nicht gefunden. Bitte versuche dich zuerst zu registrieren.",
                "info",
            )
            return render_template("accounting/register.html", form=rform)
        else:
            login_user(user, remember=form.remember_me.data)
            identity_changed.send(app, identity=Identity(str(user.id)))
            return redirect(url_for("main.index"))
    abort(404)


@main.route("/register", methods=["GET", "POST"])
def register():
    session["redirect_next"] = request.args.get(
        "next", session.get("redirect_next"))
    if request.method == "GET":
        form = RegisterForm()
        return render_template("accounting/register.html", form=form)
    if request.method == "POST":
        form = RegisterForm(request.form)
        if form.validate():
            user_email = str(form.email.data).lower()
            user = User.objects(email=user_email).first()

            if not user:
                user = User()
                form.populate_obj(user)
                user.email = user_email
                user.save()

                # noinspection PyArgumentList
                user.update(
                    push__changelog=ObjectChangelog(
                        note="Registration", data={})
                )

            login_user(user, remember=form.remember_me.data)
            identity_changed.send(app, identity=Identity(str(user.id)))
            return redirect(url_for("main.index"))

        return render_template("accounting/register.html")
    abort(404)


@main.route("/logout")
@login_required
def logout():
    # Remove the user information from the session
    logout_user()

    # Remove session keys set by Flask-Principal
    for key in ("identity.name", "identity.auth_type"):
        session.pop(key, None)

    # Tell Flask-Principal the user is anonymous
    identity_changed.send(app._get_current_object(),
                          identity=AnonymousIdentity())

    return redirect(request.args.get("next") or "/")


# Remove when adding portfolio controller
@main.route("/portfolio")
def portfolio():
    return render_template("stocks/portfolio.html")


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
            "unknown User tried to Request %s but this doesn't exist" % request.endpoint
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
