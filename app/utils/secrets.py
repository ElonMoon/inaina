import json
import os

import boto3
from django.utils.functional import LazyObject

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)

SECRETS_PATH = os.path.join(ROOT_DIR, "secrets.json")

__all__ = ("SECRETS",)


class LazySecrets(LazyObject):
    @staticmethod
    def get_secrets():
        try:
            secrets = json.load(open(SECRETS_PATH, "rt"))
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            access_key = os.environ["AWS_S3_ACCESS_KEY_ID"]
            secret_key = os.environ["AWS_S3_SECRET_ACCESS_KEY"]
            s3 = boto3.client("s3", aws_access_key_id=access_key, aws_secret_access_key=secret_key)
            s3.Object("inaina", "secrets.json").download_file(SECRETS_PATH)
            secrets = json.load(open(SECRETS_PATH, "rt"))
        return secrets

    def _setup(self):
        self._wrapped = self.get_secrets()


SECRETS = LazySecrets()
