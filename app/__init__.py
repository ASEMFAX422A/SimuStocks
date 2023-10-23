import json
import logging
import os
from flask import Flask, session, request, g, redirect, url_for, render_template
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

#db = MongoEngine(app)
#app.session_interface = MongoEngineSessionInterface(db)


from . import controllers
