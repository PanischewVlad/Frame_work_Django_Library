from django.urls import path
from .views import add_book, book_list, books_by_genre, genres_by_author, first_five_books

urlpatterns = [
    path('add_book/', add_book, name='add_book'),
    path('book_list/', book_list, name='book_list'),
    path('books_by_genre/', books_by_genre, name='books_by_genre'),
    path('genres_by_author/', genres_by_author, name='genres_by_author'),
    path('first_five_books/', first_five_books, name='first_five_books'),
]
