# Generated by Django 3.0.7 on 2020-07-21 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publishing', '0001_initial'),
        ('authors', '0001_initial'),
        ('genres', '0003_auto_20200703_0515'),
        ('books', '0020_auto_20200722_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authors.Author', verbose_name='Автор книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genres.Genre', verbose_name='Жанр книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publishing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publishing.Publishing', verbose_name='Издательство'),
        ),
    ]
