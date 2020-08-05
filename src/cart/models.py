from django.db import models
from django.contrib.auth import get_user_model
from books.models import Book
from django.urls import reverse_lazy

User = get_user_model()

class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='carts',
        blank = True,
        null = True
    )

    def __str__(self):
        return f'Cart #{self.pk}'

    @property
    def price(self):
        price = 0
        for product in self.books.all():
            price += int(product.price)
        return price

class BookInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='books'
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='books_in_cart'
    )
    quantity = models.IntegerField(
        verbose_name='Количество',
        default=1
    )

    def __str__(self):
        return f'Книга {self.book.name}'

    @property
    def price(self):
        price = self.quantity * self.book.price
        return price

    class Meta:
        unique_together = (('cart','book'),)

    def get_absolute_url(self):
        return reverse_lazy('cart:cart')