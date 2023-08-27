from django.shortcuts import redirect, render, get_object_or_404
from .models import CustomUser,TalkRoom
from .forms import SignupCustomUser,LoginCustomUser,TalkRoomForm,ChangeUsernameForm,ChangeEmailForm,ChangeIconForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from . import forms
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

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
    msg = []
    try:
        for a in obj:
            message = TalkRoom.objects.filter(Q(sender=request.user, receiver=a) | Q(sender=a, receiver=request.user)).first()
            if message:
                msg.append(message)
    except ValueError:
        print("error")
    if request.POST:
        q = request.POST["q"]
        obj = CustomUser.objects.filter(username__icontains=q).order_by('-date_joined')
        msg = []
        try:
            for a in obj:
                message = TalkRoom.objects.filter(Q(sender=request.user, receiver=a) | Q(sender=a, receiver=request.user)).first()
                if message:
                    msg.append(message)
        except ValueError:
                print("error")
    context = {'user_list':obj, 'latest_message':msg}
    return render(request, template_name, context)

@login_required
def talk_room(request, room):
    template_name = "myapp/talk_room.html"
    friend = CustomUser.objects.get(id=room)
    Messages = TalkRoom.objects.filter(Q(sender=request.user, receiver=friend) | Q(sender=friend, receiver=request.user)).order_by('date_send')
    if request.POST:
        form = TalkRoomForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = friend
            message.save()
            form = TalkRoomForm()
    else:
        form = TalkRoomForm()
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


class Logout(LoginRequiredMixin, LogoutView):
    template_name = "myapp/logout.html"

class change_username(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = ChangeUsernameForm()
        context = {"form":form}
        return render(request, 'myapp/change_username.html', context)
    
    def post(self, request, *args, **kwargs):
        form = ChangeUsernameForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            user_obj = CustomUser.objects.get(username=request.user.username)
            user_obj.username = username
            user_obj.save()
            context = {"message":"ユーザー名変更完了"}
            return render(request, 'myapp/change_username.html', context)
        else:
            context = {"form":form, "message":"ユーザー名変更失敗"}
            return render(request, 'myapp/change_username.html', context)
        
class change_email(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = ChangeEmailForm()
        context = {"form":form}
        return render(request, 'myapp/change_email.html', context)
    
    def post(self, request, *args, **kwargs):
        form = ChangeEmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            user_obj = CustomUser.objects.get(username=request.user.email)
            user_obj.email = email
            user_obj.save()
            context = {"message":"メールアドレス変更完了"}
            return render(request, 'myapp/change_email.html', context)
        else:
            context = {"form":form, "message":"メールアドレス変更失敗"}
            return render(request, 'myapp/change_email.html', context)
        
class change_icon(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = ChangeIconForm()
        context = {"form":form}
        return render(request, 'myapp/change_icon.html', context)
    
    def post(self, request, *args, **kwargs):
        form = ChangeUsernameForm(request.POST)
        if form.is_valid():
            icon = form.cleaned_data["img"]
            user_obj = CustomUser.objects.get(username=request.user.img)
            user_obj.img = icon
            user_obj.save()
            context = {"message":"アイコン変更完了"}
            return render(request, 'change_icon', context)
        else:
            context = {"form":form, "message":"アイコン変更失敗"}
            return render(request, 'change_icon', context)
        
