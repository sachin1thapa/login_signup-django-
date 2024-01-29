from django.shortcuts import render
from django.http import HttpResponse , HttpRequest ,JsonResponse
# Create your views here.

def index(request):
    # return HttpResponse('Hello this is the first page')
    return render(request , 'signup.html')