# SimuApp/app/models.py
import cryptocode

from flask import current_app as app
from . import db

from datetime import datetime, timedelta, date, time
from flask_mongoengine import BaseQuerySet
from flask_login import UserMixin, current_user


class TimestampedModel(object):
    """Mixin for keeping track of created and last modified times"""

    created = db.DateTimeField(default=datetime.now)
    modified = db.DateTimeField(default=datetime.now)


class SimuBaseModell:
    enabled = db.BooleanField(default=True)

    @classmethod
    def column_names(cls):
        return [k for k in cls._fields]

    @property
    def public_id(self):
        return cryptocode.encrypt(str(self.id), app.config["PUBLIC_ID_KEY"])


class ObjectChangelog(db.EmbeddedDocument, SimuBaseModell):
    time = db.DateTimeField(default=datetime.now)
    modified_by = db.ReferenceField("User")
    note = db.StringField()
    data = db.DictField()


class AppRun(db.DynamicDocument):
    meta = {"collection": "app_run"}
    time = db.DateTimeField(default=datetime.now)

    version = db.StringField(
        required=True
    )  # Like 1.0.0-DEV-202012201200 (the last is date and time)
    # Format of the date is YYYY MM DD HH MM SS without blanks

    version_id = db.StringField(required=True)  # Version Like 1.0.0

    mode = db.StringField(required=True)  # The App mode, like DEV, PROD, TEST.
    # Typically you can get this information already form the Database


class ApplicationLog(db.DynamicDocument):
    meta = {"collection": "application_logs"}
    time = db.DateTimeField(default=datetime.now)  # created

    levelname = db.StringField(required=True)  # The levelname of the Log.
    # See https://docs.python.org/3/howto/logging.html#logging-levels for more information

    module = db.StringField(required=True)  # module
    msg = db.StringField(required=True)  # msg
    appRun = db.ReferenceField("AppRun", required=True)


class Stocks(db.DynamicDocument):
    meta = {"collection": "Prices"}

    ticker = db.StringField(required=True)
    data = db.ListField()

    @property
    def ticker_name(self):
        return self.ticker

    @property
    def ticker_data(self):
        return self.data


class User(UserMixin, db.Document, SimuBaseModell):
    firstname = db.StringField(required=True)
    lastname = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)

    login_times = db.ListField(db.DateTimeField(default=datetime.now))

    enabled = db.BooleanField(default=True)
    changelog = db.EmbeddedDocumentListField(ObjectChangelog)

    @property
    def last_login(self):
        if len(self.login_times) > 0:
            return self.login_times[-1]
        else:
            return None

    @property
    def full_name(self):
        return self.firstname + " " + self.lastname

    @property
    def full_name_rev(self):
        return self.firstname + ", " + self.lastname
