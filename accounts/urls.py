from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^join/$', join, name='join'),
    url(r'^login/$', signin, name='login'),
    path('pleaseLogin', pleaseLogin),
    path('pleaseLogout', pleaseLogout),
    path('logout', signout),
]