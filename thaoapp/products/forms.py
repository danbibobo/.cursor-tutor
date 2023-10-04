from django import forms
from .models import Book

class Book_Form(forms.ModelForm):
    class Meta:
        model = Book
        fields =  ['name', 'author','author_email','price']
