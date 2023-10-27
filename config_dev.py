import datetime

# Fetch default settings
from config_default import *

SIMU_MODE = "dev"

MONGODB_DB = "simu_dev"
MONGODB_HOST = "localhost"
MONGODB_PORT = 27017

DEBUG = True

SECRET_KEY = "gQ|g(@+Dy.pPOzlsad6daada|9K.j?dsQ8P)9X[Pm(@:#.SQRI7>ZZ[r)tT"

VERSION = VERSION + "-DEV-" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
