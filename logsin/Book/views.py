from .form import MyForm
from django.shortcuts import render  , redirect
from django.http import request, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Book
from django.contrib.auth.models import User

# from logsin


# Create your views here.


@login_required(login_url='login')
def library(request):
    books = Book.objects.all()

    return render(request, 'library.html', {'user': request.user, 'book': books})


def my_view(request):
    print('user',request.user.is_superuser)
    if not request.user.is_superuser:
        return HttpResponse(" bak muji")

    form = MyForm()
    return render(request, 'lib_add.html', {'form': form})


def libdata(request):
    print('user',request.user.is_superuser)
    if not request.user.is_superuser:
        return HttpResponse(" bak muji")


    if request.method == 'POST':
        name = request.POST.get('name')
        img =  request.FILES.get('img')
        author = request.POST.get('author')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        offer = request.POST.get('offer') == 'on'

        book = Book.objects.create(name = name , img = img , author = author , email = email ,desc =  desc ,offer =  offer)

    return redirect('bookhome')



