from django.shortcuts import render
from django.http import request , HttpResponse


# Create your views here.

def library(request):
    return render(request , 'library.html')