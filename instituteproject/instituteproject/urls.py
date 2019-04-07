"""instituteproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:

"""
from django.conf.urls import url
from django.contrib import admin
from instituteapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home),
    url(r'^home/',views.home),
    url(r'^contact/',views.contact),
    url(r'^services/',views.services),
    url(r'^feedback/',views.feedback),
    url(r'^gallery/',views.gallery)
]
