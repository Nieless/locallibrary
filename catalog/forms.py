from django import forms
from django.forms.models import inlineformset_factory
from .models import Author, Book
from .helpers import book_helper


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['summary'].label = False
        self.helper = book_helper


class BookSearchForm(forms.Form):
    name = forms.CharField(max_length=100)


Bookformset = inlineformset_factory(Author, Book, BookForm, extra=2)
