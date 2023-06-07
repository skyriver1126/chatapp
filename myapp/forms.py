from django import forms
from .models import CustomUser

class SignupCustomUser(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'img')