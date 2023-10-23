import json
import logging
import os
from flask import Flask, session, request, g, redirect, url_for, render_template
from flask_login import LoginManager, AnonymousUserMixin, current_user
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_socketio import SocketIO, disconnect
from flask_wtf import CSRFProtect
from logging import StreamHandler, Formatter
from logging.handlers import SMTPHandler

app = Flask(__name__)

configs = {
    'dev': 'config_dev',
    'test': 'config_test',
    'prod': 'config_prod'
}

mode = os.environ.get('SIMU_MODE', 'dev')
app.config.from_object(configs[mode])

db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)

login_manager = LoginManager()

from .models import *

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
mongologger.setFormatter(Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
app.logger.addHandler(mongologger)

login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message = None
login_manager.anonymous_user = Anonymous

from . import controllers
