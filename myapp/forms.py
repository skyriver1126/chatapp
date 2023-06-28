from typing import Any
from django import forms
from .models import CustomUser
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
        
    # def clean(self):
    #     username = self.cleaned_data.get("username")
    #     password = self.cleaned_data.get("password")

    #     if username is not None and password:
    #         self.user_cache2 = authenticate(
    #             self.request, username=username
    #         )
    #         self.user_cache = authenticate(
    #             self.request, username=username, password=password
    #         )
    #         if self.user_cache2 is None:
    #             raise self.get_user_error()
    #         else:
    #             if self.user_cache is None:
    #                 raise self.get_invalid_login_error()
    #             else:
    #                 self.confirm_login_allowed(self.user_cache2)

    #     return self.cleaned_data



        
