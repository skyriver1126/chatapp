from django.shortcuts import redirect, render, get_object_or_404
from .models import CustomUser
from .forms import SignupCustomUser,LoginCustomUser,SearchForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from . import forms
from django.db.models import Q


def index(request):
    return render(request, "myapp/index.html")

def signup_view(request):
    return render(request, "myapp/signup.html")

def login_view(request):
    return render(request, "myapp/login.html")

@login_required
def friends(request):
    template_name = "myapp/friends.html"
    obj = CustomUser.objects.exclude(username=request.user.username).order_by('-date_joined')
    keyword = request.GET.get('keyword')
    if keyword:
        obj = CustomUser.filter(Q(username_icontains=keyword))
    context = {'obj_list':obj}
    return render(request, template_name, context)

@login_required
def talk_room(request,room):
    template_name = "myapp/talk_room.html"
    return render(request, template_name)

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

