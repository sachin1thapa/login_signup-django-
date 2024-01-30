from django.shortcuts import render
from django.http import HttpResponse , HttpRequest ,JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return HttpResponse('This is the home page hello!!')

def signup(request):
    return render(request , 'signup.html')

def login(request):
    return render(request , 'login.html')


def sign(request):
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

    

        