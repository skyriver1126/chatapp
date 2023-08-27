from typing import Any
from django import forms
from .models import CustomUser,TalkRoom
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.views import LoginView
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

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
        self.user_cache2 = None

    def get_user_error(self):
        return ValidationError(
            self.error_messages["inactive"],
            code="inactive"
        )
    
    def get_invalid_login_error(self):
        return ValidationError(
            self.error_messages["invalid_login"],
            code="invalid_login"
        )

class TalkRoomForm(forms.ModelForm):
    class Meta:
        model = TalkRoom
        fields = ('message',)

class ChangeEmailForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("email",)

class ChangeIconForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("img",)

class ChangeUsernameForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("username",)

