# Generated by Django 3.0.4 on 2020-03-16 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinsaat', '0016_auto_20200316_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=150, null=True, unique=True)),
                ('image', models.ImageField(upload_to='uploads/portfolio')),
            ],
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='image',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='image',
            field=models.ManyToManyField(related_name='photo', to='tinsaat.Gallery'),
        ),
    ]
