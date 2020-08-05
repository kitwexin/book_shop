from django.db import models
from genres.models import Genre
from authors.models import Author
from publishing.models import Publishing

class Book(models.Model):
    name = models.CharField(
        verbose_name='Название книги',
        max_length=50
    )
    price = models.IntegerField(
        verbose_name='Стоимость книги BYN',
        default='0'
        )
    post_year = models.IntegerField(
        verbose_name='Год издания',
        null=True,
        blank=True
    )
    image = models.ImageField(
        verbose_name="Фото обложки",
        upload_to="books-pics",
        null=True,
        blank=True
    )
    pages = models.IntegerField(
        verbose_name='Количество страниц',
        default='0'
    )
    binding = models.CharField(
        verbose_name='Переплет',
        max_length=20,
        null=True,
        blank=True
    )
    weight = models.CharField(
        verbose_name='Вес',
        max_length=20,
        null=True,
        blank=True
    )
    age_limit = models.CharField(
        verbose_name='Возрастное ограничение',
        default='0+',
        max_length=10,
    )
    form = models.CharField(
        verbose_name='Формат',
        max_length=20,
        null=True,
        blank=True
    )
    isbn = models.CharField(
        verbose_name='ISBN',
        max_length=20,
        null=True,
        blank=True
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        verbose_name='Жанр книги'
    )
    publishing = models.ForeignKey(
        Publishing,
        on_delete=models.CASCADE,
        verbose_name='Издательство'
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        verbose_name='Автор книги'
    )
    description = models.TextField(
        verbose_name='Описание книги'
    )
    available = models.CharField(
        verbose_name='Количество в наличии',
        max_length=10,
        default=1
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/books/list-books/'

