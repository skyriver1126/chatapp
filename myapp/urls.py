from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup_view'),
    path('accounts/',include('allauth.urls')),
    path('login', views.Login.as_view(), name='login_view'),
    path('friends', views.friends, name='friends'),
    path('talk_room/<int:room>', views.talk_room, name='talk_room'),
    path('setting', views.setting, name='setting'),
    path('logout', views.Logout.as_view(), name='logout_view'),
    path('change_username', views.change_username.as_view(), name='change_username'),
    path('change_email', views.change_email.as_view(), name='change_email'),
    path('change_icon', views.change_icon.as_view(), name='change_icon'),
    path('change_password', views.change_password.as_view(), name='change_password'),
    path('password_change_done', views.password_change_done.as_view(), name='password_change_done'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)