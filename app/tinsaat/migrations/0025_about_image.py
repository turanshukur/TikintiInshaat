# Generated by Django 3.0.4 on 2020-03-17 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinsaat', '0024_remove_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
    ]
