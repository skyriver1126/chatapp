from django.shortcuts import redirect, render, get_object_or_404
from .models import CustomUser
from .forms import SignupCustomUser,LoginCustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from . import forms


def index(request):
    return render(request, "myapp/index.html")

def signup_view(request):
    return render(request, "myapp/signup.html")

def login_view(request):
    return render(request, "myapp/login.html")

@login_required
def friends(request):
    template_name = "myapp/friends.html"
    obj = CustomUser.objects.exclude(username=request.user.username)
    context = {'obj_list':obj}
    return render(request, template_name, context)

@login_required
def talk_room(request):
    return render(request, "myapp/talk_room.html")

def setting(request):
    return render(request, "myapp/setting.html")

def signup(request):
    if request.POST:
        form = SignupCustomUser(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return  redirect(index)
    else:
        form = SignupCustomUser
    return render(request, "myapp/signup.html", {'form': form})

class Login(LoginView):
    form_class = forms.LoginCustomUser
    template_name = "myapp/login.html"

