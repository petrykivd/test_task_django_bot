from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(models.Model):
    tg_user_id = models.IntegerField(unique=True, null=False)
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    chat_id = models.IntegerField(null=False, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
