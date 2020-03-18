# Generated by Django 3.0.4 on 2020-03-15 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinsaat', '0009_auto_20200315_1955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='data_filter',
        ),
        migrations.AddField(
            model_name='services',
            name='icons',
            field=models.CharField(choices=[('fa fa-wrench', 'fa fa-wrench'), ('fa fa-cogs', 'fa fa-cogs'), ('fa fa-cog', 'fa fa-cog'), ('fa fa-heart', 'fa fa-heart'), ('fa fa-paint-brush', 'fa fa-paint-brush')], default='fa fa-wrench', max_length=20),
        ),
    ]
