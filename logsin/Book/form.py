# forms.py
from django import forms
from .models import Book

class MyForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'img', 'author' ,'email' , 'desc' , 'offer']
