"""insaat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from tinsaat.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='main_page_url'),
    path('haqqimizda/', about_page, name='about_page_url'),
    path('xidmetler/', services_page, name='services_page_url'),
    path('portfolio/', portfolio_page, name='portfolio_page_url'),
    path('portfolio/<str:slug>/', portfolio_detail_page,
         name='portfolio_detail_page_url'),
    path('qalereya/', gallery_page, name='gallery_page_url'),
    path('contact/', ContactPageView.as_view(), name='contact_page_url'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
