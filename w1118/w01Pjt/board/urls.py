
from django.contrib import admin
from django.urls import path, include
from . import views

# app_name 은 네임으로 url 연결 시 사용
app_name = 'list'
urlpatterns = [
    # 학생입력페이지
    path('list/', views.list, name='list'),
]
