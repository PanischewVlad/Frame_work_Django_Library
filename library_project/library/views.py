from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book, Genre, Author

def book_list(request):
    books = Book.objects.all()  # Отримуємо всі книги з бази даних
    return render(request, 'library/book_list.html', {'books': books})
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})
def books_by_genre(request):
    genres = Genre.objects.all()  # Отримуємо всі жанри
    selected_genre = request.GET.get('genre')  # Отримуємо обраний жанр із запиту

    if selected_genre:
        books = Book.objects.filter(genre__name=selected_genre)  # Фільтруємо книги за жанром
    else:
        books = Book.objects.none()  # Порожній список, якщо жанр не обрано

    return render(request, 'library/books_by_genre.html', {
        'genres': genres,
        'books': books,
        'selected_genre': selected_genre,
    })
def genres_by_author(request):
    authors = Author.objects.all()  # Отримуємо всіх авторів
    selected_author_id = request.GET.get('author_name')  # Отримуємо ID вибраного автора

    genres = []
    if selected_author_id:
        selected_author = Author.objects.get(id=selected_author_id)  # Отримуємо обраного автора
        genres = Genre.objects.filter(book__author=selected_author).distinct()  # Отримуємо жанри цього автора

    return render(request, 'library/genres_by_author.html', {
        'authors': authors,
        'genres': genres,
        'selected_author_id': selected_author_id,  # Передаємо ID вибраного автора для вибору в шаблоні
    })
def first_five_books(request):
    books = Book.objects.all()[:5]  # Отримуємо перші 5 книг
    return render(request, 'library/first_five_books.html', {'books': books})

