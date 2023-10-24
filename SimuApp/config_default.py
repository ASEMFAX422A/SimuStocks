import os
from datetime import timedelta

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

FLASK_RUN_PORT = 5000

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

MONGODB_DB = 'default'
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

WTF_CSRF_TIME_LIMIT = 36000

# set session lifetime to one hour.
# users are logged out after 8 hours of inactivity.
PERMANENT_SESSION_LIFETIME = timedelta(hours=8)

PUBLIC_ID_KEY = "oReDevVvyyplMkPSjtTVqqIaULBjvEWfzSfOvExBODmJZThhVPnhbMKkHhtPUwymgHLxIF"

# Current release info
VERSION = "0.0.1"
VERSION_ID = VERSION.replace(".", "_")


DB_VERSION = 1