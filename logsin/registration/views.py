from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpRequest ,JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    # return HttpResponse('This is the home page hello!!')
    return render(request , 'index.html')

def signup(request):
    return render(request , 'signup.html')

def loginform(request):
    return render(request , 'login.html')


def signupdata(request):
    error_message = None

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
    
        if pass1 != pass2:
            error_message = 'Password doesnot match '
        else:
            user = User.objects.create_user(username=name, email=email, password=pass1 )
            return redirect('login')
    
    return render(request , 'signup.html' , {'errmsg': error_message})



def logindata(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['pass']

        user  = authenticate(request , username = username , password = password )

        print("User:", user)

        if user  is  None:
            error_message = "Email or the Password is incorrect Re enter"
            
        else:
            login(request,user)
            return redirect('msg')
        
    return render(request , 'login.html' , {'errmsg': error_message})
    




def msg(request):
    return HttpResponse("hello you ae signin")
    

        