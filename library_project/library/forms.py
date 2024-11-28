from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['author', 'genre', 'name', 'year', 'pages']  # Включаємо всі поля
        widgets = {
            'year': forms.NumberInput(attrs={'placeholder': 'Enter the publication year'}),
            'pages': forms.NumberInput(attrs={'placeholder': 'Number of pages'}),
        }
class AuthorSearchForm(forms.Form):
    author_name = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label="Choose an author", widget=forms.Select)
