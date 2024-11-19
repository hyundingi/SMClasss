from django.contrib import admin
from students.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
  list_play = ['name','major','grade','age','gender','hobby']

admin.site.register(Student)
