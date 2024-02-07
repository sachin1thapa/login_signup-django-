from .form import MyForm
from django.shortcuts import render  , redirect , get_object_or_404
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
        # form = MyForm(request.POST, request.FILES)
        name = request.POST.get('name')
        img =  request.FILES.get('img')
        author = request.POST.get('author')
        desc = request.POST.get('desc')
        offer = request.POST.get('offer') == 'on'
        price = request.POST.get('price')

        # name = form.cleaned_data.get('name')

        if Book.objects.filter(name = name).exists():
            error_message = 'The book is already at the database'
        else:
            book = Book.objects.create(name = name , img = img , author = author  ,desc =  desc ,offer =  offer , price = price)
            # form.save()
            return redirect('bookhome')
    
    return render(request, 'lib_add.html', {'errmsg': error_message})




def update_form(request , book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES , instance = book )
        form.save()
        return redirect('bookhome')

    return render(request , 'update_form.html' , {'book':book})  


# def update_data(request):
#         form = MyForm(request.POST, request.FILES)
#         name = form.cleaned_data.get('name')
#         print(name)
#         form.save()

#         return redirect('bookhome')
    

      

