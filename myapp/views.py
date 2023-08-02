from django.shortcuts import redirect, render, get_object_or_404
from .models import CustomUser,TalkRoom
from .forms import SignupCustomUser,LoginCustomUser,TalkRoomForm
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
    if request.POST:
        q = request.POST["q"]
        obj = CustomUser.objects.filter(username__icontains=q).order_by('-date_joined')
    context = {'obj_list':obj}
    return render(request, template_name, context)

@login_required
def talk_room(request, room):
    template_name = "myapp/talk_room.html"
    friend = CustomUser.objects.get(id=room)
    Messages = TalkRoom.objects.filter(Q(sender=request.user, receiver=friend) | Q(sender=friend, receiver=request.user)).order_by('date_send')
    if request.POST:
        print(request.POST.get("message"))
        form = TalkRoomForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = friend
            message.save()
    else:
        form = TalkRoomForm
    context = {'friend': friend, 'messages': Messages, 'form':form}
    return render(request, template_name, context)

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




    