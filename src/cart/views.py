from django.shortcuts import render
from django.views.generic import UpdateView, DetailView, DeleteView
from . import models
from books.models import Book
from django.urls import reverse_lazy

def get_cart(request):
    cart_pk = request.session.get('cart_pk')
    user = request.user
    if user.is_anonymous:
        user = None
    if cart_pk is not None:
        cart_pk = int(cart_pk)
    cart, create = models.Cart.objects.get_or_create(
        pk = cart_pk,
        defaults = {
            'user':user
        },
    )
    return cart, create

class AddBookToCart(UpdateView):
    models = models.BookInCart
    template_name = 'cart/add.html'
    fields = ('quantity',)

    def get_object(self):
        book_pk = self.request.GET.get('book_pk')
        book = Book.objects.get(pk=int(book_pk))
        cart, create = get_cart(self.request)
        if create:
            self.request.session['cart_pk'] = cart.pk
        obj, create = self.models.objects.get_or_create(
            cart = cart,
            book = book,
            defaults = {},
        )
        return obj

class CartDetail(DetailView):
    model = models.Cart
    template_name = 'cart/cart.html'

    def get_object(self):
        cart = get_cart(self.request)
        cart, create = get_cart(self.request)
        if create:
            self.request.session['cart_pk'] = cart.pk
        return cart

class ProductInCartDelete(DeleteView):
    model = models.BookInCart
    template_name = 'cart/delete.html'

    def get_success_url(self):
        return reverse_lazy('cart:cart')