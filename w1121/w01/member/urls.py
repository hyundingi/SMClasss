from django.urls import path, include
from . import views

app_name = 'member'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # 회원리스트
    path('mlist/', views.mlist, name='mlist'),
    # 회원 상세페이지
    path('mview/<str:id>', views.mview, name='mview'),
    # 회원 정보 수정
    path('mupdate/<str:id>', views.mupdate, name='mupdate'),
    # 회원 정보 입력
    path('mwrite/', views.mwrite, name='mwrite'),
    path('mwrite/<str:id>', views.mdelete, name='mdelete'),
]
