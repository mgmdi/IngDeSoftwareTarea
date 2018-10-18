from django.conf.urls import url, include
from django.contrib import admin
from .views import home, register, login_user
urlpatterns = [
    url(r'^$', home),
    url(r'^register/', register),
    url(r'^accounts/profile/', home),
    url(r'^login/$', login_user),
]