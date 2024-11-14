
from django.contrib import admin
from django.urls import path, include
## . >> 현재폴더
from . import views

app_name = ''
urlpatterns = [
    path('', views.index, name = 'index'),
]
