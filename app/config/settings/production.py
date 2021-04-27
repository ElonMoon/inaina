import platform
import sys

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *

DEBUG = (
        False
        or (
            len(sys.argv) > 1
            and sys.argv[1] == "runserver"
            and platform.system() != "Linux"
        )
        or os.environ.get("DEBUG") == "True"
)
AWS_SECRETS_MANAGER_SECRET_SECTION = 'inaina:production'
AWS_STORAGE_BUCKET_NAME = SECRETS['AWS_STORAGE_BUCKET_NAME']
AWS_QUERYSTRING_AUTH = False

# Static
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'

# django-dbbackup
DBBACKUP_STORAGE = 'config.storages.DBStorage'
DBBACKUP_STORAGE_OPTIONS = {
    'access_key': SECRETS['AWS_S3_ACCESS_KEY_ID'],
    'secret_key': SECRETS['AWS_S3_SECRET_ACCESS_KEY'],
    'bucket_name': SECRETS['AWS_STORAGE_BUCKET_NAME'],
}

ALLOWED_HOSTS += SECRETS['ALLOWED_HOSTS']
DATABASES = SECRETS['DATABASES']
sentry_sdk.init(
    dsn=SECRETS['SENTRY_DSN'],
    integrations=[DjangoIntegration()]
)

WSGI_APPLICATION = 'config.wsgi.production.application'
