
from django.contrib import admin
from django.urls import path, include
from . import views

# app_name 은 네임으로 url 연결 시 사용
app_name = 'students'
urlpatterns = [
    # 학생입력페이지
    path('write/', views.write, name='write'),  # 학생입력페이지
    path('list/', views.list, name='list'),     # 학생 리스트
    # 앱네임으로 데이터 받기 (list.html)
    path('<str:name>/View/', views.View, name='View'),  # 학생 상세 정보 
    path('<str:name>/modify/', views.modify, name='modify'),  # 학생 수정 페이지 1
    path('modify2/', views.modify2, name='modify2'),  # 학생 수정 페이지 2
    path('<str:name>/modify3/', views.modify3, name='modify3'),  # 학생 수정 페이지 3
    path('<str:name>/delete/', views.delete, name='delete'),  # 학생 삭제

]
