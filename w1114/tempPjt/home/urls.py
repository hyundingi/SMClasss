from django.urls import path, include
from . import views


app_name = ''

urlpatterns = [
    ### url 주소, veiws.py함수명, url 이름
    ## http://127.0.0.1:8000/students/reg/
    # students:reg << 이런식으로 name으로 연결 가능함 (프로그램 내에서만)
    path('', views.index, name='index'),
]
