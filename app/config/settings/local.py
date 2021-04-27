from .base import *

DEBUG = True

# django-dbbackup
DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {
    'location': DB_ROOT,
}

ALLOWED_HOSTS += [
    'localhost',
    'inaina.localhost',
]
DATABASES = {
    "default": {
      "ENGINE": "django.db.backends.postgresql",
      "NAME": "inaina",
      "USER": "inaina",
      "PASSWORD": "inaina",
      "HOST": "localhost",
      "PORT": 5432
    }
}

WSGI_APPLICATION = 'config.wsgi.local.application'
