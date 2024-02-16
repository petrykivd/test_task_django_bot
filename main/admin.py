from django.contrib import admin

from main.forms import ProfileForm
from main.models import User


@admin.register(User)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "tg_user_id",
        "username",
        "first_name",
        "chat_id",
        "date_joined",
    )
    form = ProfileForm
