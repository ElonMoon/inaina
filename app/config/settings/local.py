from .base import *

import_secrets()

DEBUG = True

WSGI_APPLICATION = 'config.wsgi.local.application'
