from typing import Any
from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.views import LoginView
from django.utils.translation import gettext_lazy as _

class SignupCustomUser(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'img')

class LoginCustomUser(AuthenticationForm):
    error_messages = {
            "invalid_login": _("ユーザーID、パスワードが一致しません。"),
            "inactive": _("ユーザーが存在しません。"),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        


        
