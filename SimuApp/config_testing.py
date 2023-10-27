import os
from datetime import timedelta, datetime

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

FLASK_RUN_PORT = 5000

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

WTF_CSRF_TIME_LIMIT = 36000

# set session lifetime to one hour.
# users are logged out after 8 hours of inactivity.
PERMANENT_SESSION_LIFETIME = timedelta(hours=8)

PUBLIC_ID_KEY = "oReDevVvyyplMkPSjtTVqqIaULBjvEWfzSfOvExBODmJZThhVPnhbMKkHhtPUwymgHLxIF"

# Current release info
VERSION = "0.0.1"
VERSION_ID = VERSION.replace(".", "_")


DB_VERSION = 1

SIMU_MODE = 'testing'

MONGODB_DB = 'flaskdb'
MONGODB_HOST = 'mongodb'
MONGODB_USERNAME = 'mongodbuser'
MONGODB_PASSWORD = 'your_mongodb_root_password'
MONGODB_PORT = 27017

DEBUG = True

SECRET_KEY = 'gQ|g(@+Dy.pPOzlsad6daada|9K.j?dsQ8P)9X[Pm(@:#.SQRI7>ZZ[r)tT'

VERSION = VERSION + "-DEV-" + datetime.now().strftime('%Y%m%d%H%M%S')