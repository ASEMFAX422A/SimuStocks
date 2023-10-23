import random
import bson

from datetime import date

from dateutil.parser import parse


def is_valid_object_id(string):
    return bson.objectid.ObjectId.is_valid(string)


def random_string(length):
    return ''.join(random.choice('abcdefghjkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ123456789') for x in range(length))


def redirect_url(default='index'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)


def safe_cast(val, to_type, default=None):
    from app import app
    if type(val) == to_type:
        app.logger.debug("Tryed to convert %s of type %s to %s but its alredy" % (val, type(val), to_type))
        return val
    try:
        return to_type(val)
    except (ValueError, TypeError):
        app.logger.critical("Error on converting a Value")
        return default

