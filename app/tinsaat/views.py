from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import View
# Create your views here.


def main_page(request):
    about = About.objects.get(slug='about')
    contact = Contact.objects.all()
    portfolio = Portfolio.objects.all()
    services = Services.objects.all()
    context = {
        'contact': contact,
        'about': about,
        'portfolio': portfolio,
        'services': services
    }
    return render(request, "index.html", context)


def about_page(request):
    contact = Contact.objects.all()
    about = About.objects.get(slug='about')
    context = {
        'contact': contact,
        'about': about
    }
    return render(request, 'about.html', context)


def services_page(request):
    contact = Contact.objects.all()
    services = Services.objects.all()
    context = {
        'contact': contact,
        'services': services
    }
    return render(request, 'services.html', context)


def portfolio_page(request):
    contact = Contact.objects.all()
    portfolio = Portfolio.objects.all()
    context = {
        'contact': contact,
        'portfolio': portfolio
    }
    return render(request, 'portfolio.html', context)


def portfolio_detail_page(request, slug):
    contact = Contact.objects.all()
    portfolio_detal = Portfolio.objects.get(slug__iexact=slug)
    context = {
        'contact': contact,
        'portfolio': portfolio_detal
    }
    return render(request, 'portfolioDetail.html', context)


def gallery_page(request):
    contact = Contact.objects.all()
    gallery = Gallery.objects.all()
    context = {
        'contact': contact,
        'gallery': gallery
    }
    return render(request, 'galareya.html', context)


def contact_page(request):
    return render(request, 'contact.html')


class ContactPageView(View):
    def get(self, request, *args, **kwargs):
        contact = Contact.objects.all()
        form = MessageForm
        context = {
            'form': form,
            'contact': contact
        }
        return render(request, "contact.html", context)

    def post(self, request, *args, **kwargs):

        formPost = MessageForm(request.POST)
        form = MessageForm
        context = {
            'form': form
        }
        if formPost.is_valid():
            formPost.save()
            return render(request, "contact.html", context)
        else:
            return render(request, "contact.html")
