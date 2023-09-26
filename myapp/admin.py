from django.contrib import admin

# Register your models here.

from .models import CustomUser,TalkRoom

admin.site.register(CustomUser)
admin.site.register(TalkRoom)