# Generated by Django 3.0.4 on 2020-03-16 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinsaat', '0021_auto_20200317_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='body',
            field=models.TextField(db_index=True, max_length=5000),
        ),
    ]
