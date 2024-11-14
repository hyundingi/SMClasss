
from django.contrib import admin
from django.urls import path, include
## . >> 현재폴더
from . import views

app_name = 'students'
urlpatterns = [
    path('write/', views.write, name = 'write'),
]
