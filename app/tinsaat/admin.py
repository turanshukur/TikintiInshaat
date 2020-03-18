from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(About)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "small_text"]

    class Meta:
        model = About


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ["title", "body"]

    class Meta:
        model = Services


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ["title", "body", "slug", "date"]

    class Meta:
        model = Portfolio


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ["title"]

    class Meta:
        model = Gallery


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    readonly_fields = ["first_name", "last_name",
                       "subject", "number", "email", "body"]

    list_display = ["first_name", "last_name",
                    "subject", "number"]

    class Meta:
        model = Message


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["adress", "phone", "email"]

    class Meta:
        model = Message
