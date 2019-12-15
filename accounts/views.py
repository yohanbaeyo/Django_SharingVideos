from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.template import RequestContext

# Create your views here.
def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('로그인 실패. 다시 시도해보세요.')
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form' : form})
def join(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if request.POST['password'] == request.POST['verify_password']:
            new_user = User.objects.create_user(username=form['username'], password=form['password'])
            login(request, new_user)
            return redirect('index')
    else:
        form = UserForm()
        return render(request, 'accounts/join.html', {'form':form})

def pleaseLogin(request):
    return render(request, 'accounts/pleaseLogin.html')

def pleaseLogout(request):
    return render(request, 'accounts/pleaseLogout.html')

def signout(request):
    logout(request)
    return redirect('index')
