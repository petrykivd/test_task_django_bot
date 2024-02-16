from django import forms
from django.forms import CheckboxSelectMultiple

from main.models import User, Message


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "tg_user_id",
            "username",
            "first_name",
            "date_joined",
        )
        widgets = {
            "username": forms.TextInput,
            "first_name": forms.TextInput,

        }


class MessageForm(forms.ModelForm):
    user = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=CheckboxSelectMultiple, required=True)
    class Meta:
        model = Message
        fields = ['user', 'text']
