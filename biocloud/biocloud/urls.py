"""biocloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from pages import views
from accounts import views as account_views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^samples/', include('samples.urls')),
    url(r'^semantic_ui_doc/', include('semantic_ui_doc.urls')),
    url(r'^example_form/', include('play_form.urls'), name='example_form'),
    url(r'^accounts/register$', account_views.register, name='register'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
