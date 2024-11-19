from django.urls import path,include
from . import views

app_name = 'students'
urlpatterns = [
    # url 링크, views 에서 함수 호출, name 링크
    path('write/', views.write, name = 'write' ),
    path('list/', views.list, name = 'list' ),
    path('<str:name>/view/', views.view, name = 'view' ),
    path('update/', views.update, name = 'update' ),  # 파라미터 방식
    # path('update/<str:name>/', views.update, name = 'update' ),
    path('delete/<str:name>/', views.delete, name = 'delete' ), 
    path('search/', views.search, name = 'search' ), 
]