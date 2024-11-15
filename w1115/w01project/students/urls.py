from django.contrib import admin
from django.urls import path, include
from . import views

## app이름 : 이름으로 접근
app_name = 'students'
urlpatterns = [
  # views.py 연결 - 함수호출, app함수이름
  path('write/', views.write, name='write')

]