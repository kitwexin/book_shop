# Generated by Django 3.0.7 on 2020-07-24 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0022_auto_20200724_0111'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='available',
            field=models.CharField(default=1, max_length=10, verbose_name='Количество в наличии'),
        ),
    ]
