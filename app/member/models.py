from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager


class UserManager(BaseUserManager):
    pass


class User(AbstractUser):
    objects = UserManager()
