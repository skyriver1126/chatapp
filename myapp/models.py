from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    img = models.ImageField(default='../media_local/null_icon.png')
