from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        default=1
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=20,
        default='Ivan'
    )
    last_name = models.CharField(
        verbose_name='Имя',
        max_length=20,
        default='Ivanov'
    )
    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        default='email@email.com'
    )
    image = models.ImageField(
        verbose_name="фото пользователя",
        upload_to="profile-pics",
        null=True,
        blank=True
    )
    country = models.CharField(
        verbose_name='Страна',
        max_length=20,
        default='Беларусь'
    )
    city = models.CharField(
        verbose_name='Город',
        max_length=20,
        default='Минск'
    )
    postcode = models.CharField(
        verbose_name='Индекс',
        max_length=20,
        default='220123'
    )
    address = models.TextField(
        verbose_name='Адрес',
        max_length=20,
        default='ул.Советская 7-22'
    )

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

    def get_absolute_url(self):
        return '/'