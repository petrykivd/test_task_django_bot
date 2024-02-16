from django import forms

from main.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "tg_user_id",
            "username",
            "first_name",
            "chat_id",
            "date_joined",
        )
        widgets = {
            "username": forms.TextInput,
            "first_name": forms.TextInput,

        }
