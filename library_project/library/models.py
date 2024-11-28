from django.db import models

from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Назва жанру
    description = models.TextField(blank=True, null=True)  # Опис жанру (необов'язковий)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=50)  # Ім'я автора
    last_name = models.CharField(max_length=50)  # Прізвище автора
    birth_year = models.PositiveIntegerField()  # Рік народження

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Зв'язок з автором
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)  # Зв'язок із жанром
    name = models.CharField(max_length=200)  # Назва книги
    year = models.PositiveIntegerField()  # Рік публікації
    pages = models.PositiveIntegerField()  # Кількість сторінок

    def __str__(self):
        return self.name
