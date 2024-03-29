"""
Django settings for inaina project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
import os

from utils.secrets import SECRETS

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROOT_DIR = os.path.dirname(BASE_DIR)
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

# Config
IS_DOCKER = bool(os.environ.get("DOCKER"))
ALLOWED_HOSTS = []

# Static
STATIC_URL = "/static/"
STATIC_DIR = os.path.join(BASE_DIR, "static")
STATIC_ROOT = os.path.join(ROOT_DIR, ".static")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(ROOT_DIR, ".media")
DB_ROOT = os.path.join(ROOT_DIR, ".db")

STATICFILES_DIRS = [
    STATIC_DIR,
]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Secrets
SECRET_KEY = SECRETS["base"]["SECRET_KEY"]
AWS_DEFAULT_ACL = "public-read"
AWS_BUCKET_ACL = SECRETS["base"]["AWS_BUCKET_ACL"]
AWS_AUTO_CREATE_BUCKET = SECRETS["base"]["AWS_AUTO_CREATE_BUCKET"]
AWS_S3_FILE_OVERWRITE = SECRETS["base"]["AWS_S3_FILE_OVERWRITE"]

# AWS
AWS_S3_SIGNATURE_VERSION = "s3v4"
AWS_S3_REGION_NAME = "ap-northeast-2"

# Auth
AUTH_USER_MODEL = "member.User"

SITE_ID = 1

# Application definition
INSTALLED_APPS = [
    "mina",
    "jina",
    "member",
    "notice",
    "photos",
    "utils",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "colorfield",
    "dbbackup",
    "django_extensions",
    "django_quill",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            TEMPLATE_DIR,
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "config.context_processors.contexts",
            ],
        },
    },
]

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ko-kr"
TIME_ZONE = "Asia/Seoul"
USE_I18N = True
USE_L10N = True
USE_TZ = True

ROOT_URLCONF = "config.urls"
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
