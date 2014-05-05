import os
from socket import gethostname


# Project relative -> absolute root path
_PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__)).replace('\\', '/')

# Development hostnames, auto-switch to DEBUG mode
DEV_HOSTS = ('Sun', )

# Administrator auth
LOGIN = 'demo'
PASSWORD = 'demo'

SECRET_KEY = "random.get()"

# Auto switch to debug?
DEBUG = gethostname() in DEV_HOSTS

SQLALCHEMY_DATABASE_URI = "sqlite:///" + _PROJECT_ROOT + "/database.sqlite3"
