from django.db import models

class Publishing(models.Model):
    name = models.CharField(
        verbose_name='Издательство',
        max_length=50,
        default='...'
    )
    description = models.TextField(
        verbose_name='Описание издательства',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/publishing/list/'