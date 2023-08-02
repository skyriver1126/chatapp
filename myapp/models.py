from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    img = models.ImageField(default='null_icon.png')

class TalkRoom(models.Model):
    message = models.CharField('message',max_length=150)
    sender = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name="sent_talk")
    receiver = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name="received_talk")
    date_send = models.DateTimeField(_("date send"), default=timezone.now)
