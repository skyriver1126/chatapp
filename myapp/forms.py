from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

class SignupCustomUser(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'img')

class LoginCustomUser(LoginView):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

        
