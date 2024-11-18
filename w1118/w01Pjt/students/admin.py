from django.contrib import admin
from students.models import Student

# admin 페이지에서 보여지는 부분
class StudentAdmin(admin.ModelAdmin):
  list_display = ['name', 'major', 'grade', 'age', 'gender']
# admin 페이지에 model 등록
admin.site.register(Student, StudentAdmin)

