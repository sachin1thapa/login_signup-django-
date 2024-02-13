from .form import MyForm
from django.shortcuts import render  , redirect , get_object_or_404
from django.http import request, HttpResponse , JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Book
from django.contrib.auth.models import User 
from django.db.models import Q


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

        # if form.is_valid():
        #     name = form.cleaned_data.get('name')
        #     print(name)
        form = MyForm()
        if Book.objects.filter(name = name).exists():
            error_message = 'The book is already at the database'
        else:
            book = Book.objects.create(name = name , img = img , author = author  ,desc =  desc ,offer =  offer , price = price)
            # form.save()
            return redirect('bookhome')
    
    return render(request, 'lib_add.html', {'errmsg': error_message,'form':form})



@login_required(login_url='login')
def update_form(request , book_id):
    if not request.user.is_superuser:
        return HttpResponse(" bak muji j paye tei garchas")
     

    # book = Book.objects.get(id=book_id)       yesari panai linw milcha tarw yesle rerror handel gardeae nw 
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES , instance = book )
        form.save()
        return redirect('bookhome')

    return render(request , 'update_form.html' , {'book':book})  


@login_required(login_url='login')
def remove(request , remove_id):
    if not request.user.is_superuser:
        return HttpResponse(" bak muji j paye tei garchas")
    
    book = get_object_or_404(Book, id=remove_id)
    book.delete()
    return redirect('bookhome')

      

def search(request):
        book_name = request.GET.get('name')
        search_result = Book.objects.filter(Q(name__icontains=book_name)|Q(author__icontains =book_name ))
        if search_result.exists():
        # search_result =  Book.objects.filter(__name__icontains = book_name))            # single ko lagi ko lagi     
            return render(request, 'library.html' ,{'user': request.user, 'book': search_result} )
        else:
            return HttpResponse("No data is available")


            
            







