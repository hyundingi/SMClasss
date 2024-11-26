"""
URL configuration for w01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'board'
urlpatterns = [
    path('blist/', views.blist, name='blist'),
    path('bwrite/', views.bwrite, name='bwrite'),
    path('bview/<int:bno>/', views.bview, name='bview'),
    path('bdelete/<int:bno>/', views.bdelete, name='bdelete'),
    path('bupdate/<int:bno>/', views.bupdate, name='bupdate'),
    path('breply/<str:bno>/', views.breply, name='breply'),
]

