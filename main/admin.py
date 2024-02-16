import logging

from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from main.forms import ProfileForm, MessageForm

from main.models import User, Message
from main.utils import send_message_sync


logger = logging.getLogger('django_admin')


@admin.register(User)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "tg_user_id",
        "username",
        "first_name",
        "date_joined",
        "send_message_button",
    )
    form = ProfileForm

    def send_message_button(self, obj):
        url = reverse("admin:main_message_add")
        return mark_safe(f'<a href="{url}?user={obj.id}">Send message</a>')

    send_message_button.allow_tags = True
    send_message_button.short_description = 'Actions'


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['display_users', 'text', 'created_at']
    form = MessageForm

    def display_users(self, obj):
        return ", ".join([user.username for user in obj.user.all()])
    display_users.short_description = 'Sent to users'

    def response_add(self, request, obj, post_url_continue=None):
        for user in obj.user.all():
            send_message_sync(user.tg_user_id, obj.text)
            logger.info(f"Admin {request.user.username} sent message '{obj.text}' to user {user.username}")
        return super().response_add(request, obj, post_url_continue)

    def has_change_permission(self, request, obj=None):
        return False
