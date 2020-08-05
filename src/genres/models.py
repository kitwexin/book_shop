from django.db import models

class Genre(models.Model):
    name = models.CharField(
        verbose_name='Название жанра',
        max_length=20,
        null=True,
        blank=True
    )
    description = models.TextField(
        verbose_name='Описание жанра',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/genre/list-genre/'