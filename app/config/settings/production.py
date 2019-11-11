import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *

AWS_SECRETS_MANAGER_SECRETS_SECTION = 'inaina:production'
DEBUG = False

ALLOWED_HOSTS += SECRETS['ALLOWED_HOSTS']
DATABASES = SECRETS['DATABASES']
sentry_sdk.init(
    dsn=SECRETS['SENTRY_DSN'],
    integrations=[DjangoIntegration()]
)

WSGI_APPLICATION = 'config.wsgi.production.application'
