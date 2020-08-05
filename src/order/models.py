from django.db import models
from cart.models import Cart

class Order(models.Model):
    cart = models.OneToOneField(
        Cart,
        on_delete=models.PROTECT,
        related_name='order'
    )
    status = models.BooleanField(
        'Is complete',
        default = False
    )
    delivery_address = models.TextField('Адрес доставки')
    contact_phone = models.CharField('Контактный телефон',max_length=13)
    created = models.DateTimeField(
        'Created',
        auto_now=False,
        auto_now_add=True
    )
    updated = models.DateTimeField(
        'Updated',
        auto_now=True,
        auto_now_add=False
    )

    def __str__(self):
        return str(self.pk)