from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .models import Userdata


# Create your views here.
def home(request):
    # return HttpResponse('This is the home page hello!!')
    return render(request, 'index.html', {'user': request.user})


def signup(request):
    return render(request, 'signup.html')


def loginform(request):
    return render(request, 'login.html')


def signupdata(request):
    error_message = None

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        hashed_password = make_password(pass1)

        if pass1 != pass2:
            error_message = 'Password doesnot match '
        else:
            if Userdata.objects.filter(name = name ).exists():
                error_message = "Name already Used  "
            elif Userdata.objects.filter(email = email ).exists():
                error_message = "Email already taken"
            else : 
                user = Userdata.objects.create(name=name, email=email, password=hashed_password)
                return redirect('login')

    return render(request, 'signup.html', {'errmsg': error_message})


def logindata(request):
    error_message = None

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']

        user = authenticate(request, username=email, password=password)

        print("User:", user)

        if user is None:
            error_message = "Email or the Password is incorrect Re enter"
        else:
            login(request, user)
            return redirect('name')

    return render(request, 'login.html', {'errmsg': error_message})


def msg(request):
    return HttpResponse("hello you ae signin")


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')
