from .base import *

import_secrets()

DEBUG = False

WSGI_APPLICATION = 'config.wsgi.production.application'
