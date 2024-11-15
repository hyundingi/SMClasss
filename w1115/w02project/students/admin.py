from django.contrib import admin
from students.models import Student

## admin 사이트에서 컬럼부분 노출 설정
class StudentAdmin(admin.ModelAdmin):
  list_display = ['s_name', 's_major','s_age']

# Register your models here.
## admin 사이트에 추가
admin.site.register(Student, StudentAdmin)
