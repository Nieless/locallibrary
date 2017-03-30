from django import forms
from django.forms.models import inlineformset_factory
from .models import Author, Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


Bookformset = inlineformset_factory(Author, Book, BookForm, extra=2)
