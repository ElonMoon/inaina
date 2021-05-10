from .production import *

DEBUG = True

AWS_STORAGE_BUCKET_NAME = SECRETS["AWS_STORAGE_BUCKET_NAME"]

# django-dbbackup
DBBACKUP_STORAGE = "config.storages.DBStorage"
DBBACKUP_STORAGE_OPTIONS = {
    "access_key": SECRETS["AWS_S3_ACCESS_KEY_ID"],
    "secret_key": SECRETS["AWS_S3_SECRET_ACCESS_KEY"],
    "bucket_name": SECRETS["AWS_STORAGE_BUCKET_NAME"],
}

ALLOWED_HOSTS += SECRETS["ALLOWED_HOSTS"]
DATABASES = SECRETS["DATABASES"]
sentry_sdk.init(dsn=SECRETS["SENTRY_DSN"], integrations=[DjangoIntegration()])

WSGI_APPLICATION = "config.wsgi.develop.application"
