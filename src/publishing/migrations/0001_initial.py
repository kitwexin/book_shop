# Generated by Django 3.0.7 on 2020-07-09 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publishing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='...', max_length=50, verbose_name='Издательство')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание издательства')),
            ],
        ),
    ]
