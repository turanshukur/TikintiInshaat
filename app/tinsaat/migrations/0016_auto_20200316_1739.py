# Generated by Django 3.0.4 on 2020-03-16 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinsaat', '0015_auto_20200316_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=150, null=True, unique=True),
        ),
    ]
