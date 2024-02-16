from django.db import models
from django.utils import timezone


class User(models.Model):
    tg_user_id = models.IntegerField(unique=True, null=False)
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"#{self.tg_user_id} {self.username}"

    class Meta:
        verbose_name = "Telegram User"
        verbose_name_plural = "Telegram Users"


class Message(models.Model):
    user = models.ManyToManyField(User, related_name="messages")
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Message to {self.user} at {self.created_at}'

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
