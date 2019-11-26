from django import forms
from Library.models import Book


class LibraryForm(forms.ModelForm):
    post = forms.CharField()

    class Meta:
        model = Book
        fields = ('book_name','course',)
