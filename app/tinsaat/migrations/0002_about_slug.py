# Generated by Django 3.0.4 on 2020-03-14 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinsaat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='slug',
            field=models.SlugField(default='about', max_length=10, unique=True),
        ),
    ]
