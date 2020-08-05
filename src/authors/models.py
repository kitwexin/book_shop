from django.db import models

class Author(models.Model):
    name = models.CharField(
        verbose_name='Автор',
        max_length=20,
        null=True,
        blank=True
    )
    description = models.TextField(
        verbose_name='Описание автора',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/author/list-authors/'