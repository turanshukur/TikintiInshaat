from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator

# Create your models here.


class About(models.Model):
    slug = models.SlugField(max_length=10, unique=True,
                            default='about', editable=False)
    title = models.CharField(max_length=50, db_index=True)
    small_text = models.CharField(max_length=150, db_index=True)
    body = models.TextField(blank=True, db_index=True)
    image = models.ImageField(upload_to='uploads/', blank=True)


class Services(models.Model):
    classes = (
        ('fa fa-wrench', 'fa fa-wrench'),
        ('fa fa-cogs', 'fa fa-cogs'),
        ('fa fa-cog', 'fa fa-cog'),
        ('fa fa-heart', 'fa fa-heart'),
        ('fa fa-paint-brush', 'fa fa-paint-brush'),
    )
    icons = models.CharField(
        max_length=20, choices=classes, default='fa fa-wrench')
    title = models.CharField(max_length=50, db_index=True)
    body = models.TextField(blank=True, db_index=True)
    upload = models.ImageField(upload_to='uploads/')


class Portfolio(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, null=True,
                            blank=True, unique=True, editable=False)
    body = models.TextField(blank=True, db_index=True)
    base_image = models.ImageField(
        upload_to='uploads/portfolio/base', null=True, blank=True)
    image = models.ManyToManyField("Gallery", related_name="photo")
    date = models.DateField()

    def __str__(self):
        return self.title


def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_save, sender=Portfolio)


class Gallery(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, null=True,
                            blank=True, unique=True, editable=False)
    image = models.ImageField(upload_to='uploads/portfolio')

    def __str__(self):
        return self.title


class Message(models.Model):
    first_name = models.CharField(max_length=150, db_index=True)
    last_name = models.CharField(max_length=150, db_index=True)
    email = models.EmailField(max_length=150, db_index=True)
    subject = models.CharField(max_length=150, db_index=True)
    number = models.CharField(max_length=150, db_index=True)
    body = models.TextField(max_length=5000, db_index=True)


class Contact(models.Model):
    adress = models.CharField(max_length=250, db_index=True)
    phone = models.CharField(max_length=250, db_index=True)
    email = models.EmailField(max_length=250, db_index=True)
