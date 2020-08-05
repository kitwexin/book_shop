# Generated by Django 3.0.7 on 2020-07-08 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
        ('genres', '0003_auto_20200703_0515'),
        ('books', '0009_auto_20200704_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(blank=True, null=True, to='authors.Author', verbose_name='Автор книги'),
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(blank=True, null=True, to='genres.Genre', verbose_name='Жанр книги'),
        ),
    ]