
from django.contrib import admin
from django.urls import path, include
## . >> 현재폴더
from . import views

app_name = 'event'
urlpatterns = [
    path('eventView/', views.eventView, name = 'eventView'),
]
