from django import forms
from .models import Book

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'data-text': ''}),
        }