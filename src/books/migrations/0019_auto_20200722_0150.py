# Generated by Django 3.0.7 on 2020-07-21 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publishing', '0001_initial'),
        ('genres', '0003_auto_20200703_0515'),
        ('authors', '0001_initial'),
        ('books', '0018_auto_20200722_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, to='authors.Author', verbose_name='Автор книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, to='genres.Genre', verbose_name='Жанр книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publishing',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, to='publishing.Publishing', verbose_name='Издательство'),
        ),
    ]
