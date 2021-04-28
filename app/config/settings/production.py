import platform
import sys

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *

DEBUG = (
    False
    or (len(sys.argv) > 1 and sys.argv[1] == "runserver" and platform.system() != "Linux")
    or os.environ.get("DEBUG") == "True"
)
AWS_STORAGE_BUCKET_NAME = SECRETS["production"]["AWS_STORAGE_BUCKET_NAME"]
AWS_QUERYSTRING_AUTH = False

# Static
DEFAULT_FILE_STORAGE = "config.storages.MediaStorage"

# django-dbbackup
DBBACKUP_STORAGE = "config.storages.DBStorage"
DBBACKUP_STORAGE_OPTIONS = {
    "access_key": SECRETS["production"]["AWS_S3_ACCESS_KEY_ID"],
    "secret_key": SECRETS["production"]["AWS_S3_SECRET_ACCESS_KEY"],
    "bucket_name": SECRETS["production"]["AWS_STORAGE_BUCKET_NAME"],
}

ALLOWED_HOSTS += SECRETS["production"]["ALLOWED_HOSTS"]
DATABASES = SECRETS["production"]["DATABASES"]
sentry_sdk.init(dsn=SECRETS["production"]["SENTRY_DSN"], integrations=[DjangoIntegration()])

WSGI_APPLICATION = "config.wsgi.production.application"
