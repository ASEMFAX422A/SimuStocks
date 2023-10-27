# SimuApp/app/__init__.py
import json
import logging, os, threading, time, mongomock
from flask import Flask, session, request, g, redirect, url_for, render_template
from flask_login import LoginManager, AnonymousUserMixin, current_user
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_socketio import SocketIO, disconnect
from flask_wtf import CSRFProtect
from logging import StreamHandler, Formatter
from logging.handlers import SMTPHandler
from datetime import datetime
from mongomock import MongoClient as MockMongoClient
from mongoengine import connect

db = MongoEngine()
login_manager = LoginManager()


def post_initialization(app):
    app.logger.debug("App has been initialized")


def create_app(testing=False):
    app = Flask(__name__)

    configs = {
        'dev': 'config_dev',
        'test': 'config_test',
        'prod': 'config_prod'
    }

    mode = os.environ.get('SIMU_MODE', 'dev')
    app.config.from_object(configs[mode])

    if testing:
        connect(db='mydb', alias='default', mongo_client_class=mongomock.MongoClient)
    else:
        db = MongoEngine()
        db.init_app(app)
        app.session_interface = MongoEngineSessionInterface(db)



    login_manager.init_app(app)
    login_manager.login_view = "login"
    login_manager.login_message = None

    from .models import AppRun, ApplicationLog

    current_run = AppRun(version=app.config["VERSION"],
                         version_id=app.config["VERSION_ID"],
                         mode=app.config['SIMU_MODE'])
    current_run.save()

    class Anonymous(AnonymousUserMixin):
        def __init__(self):
            self.name = "Anonymous User"

    class MongoHandler(StreamHandler):
        def __init__(self):
            StreamHandler.__init__(self)

        def emit(self, record):
            time = datetime.fromtimestamp(record.created)
            ApplicationLog(time=time,
                           levelname=record.levelname,
                           module=record.module,
                           msg=record.msg,
                           appRun=current_run).save()

    mongologger = MongoHandler()
    mongologger.setLevel(logging.NOTSET)
    mongologger.setFormatter(Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')) #TODO: WHY
    app.logger.addHandler(mongologger)

    def log_alive_status():
        while True:
            app.logger.debug("App is running")
            time.sleep(60)  # 60 Sekunden schlafen

    alive_thread = threading.Thread(target=log_alive_status)
    alive_thread.daemon = True  # Beenden Sie den Thread, wenn die Hauptanwendung beendet wird
    alive_thread.start()

    from .controllers import main, init_app
    init_app(login_manager)
    app.register_blueprint(main)

    post_initialization(app)

    return app
