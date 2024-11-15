from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from students.models import Student

# Create your views here.
## 학생 입력페이지 호출
def write(request):
  return render(request, 'write.html')

## 학생 전체 리스트 호출
def list(request):
  qs = Student.objects.all()
  context = {'list':qs}
  return render(request, 'list.html', context)

## 학생 리스트 저장
def save(request):
  if request.POST:
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']

    qs = Student(s_name=name, s_major=major, s_grade=grade, s_age=age, s_gender=gender)
    qs.save()
  return HttpResponseRedirect(reverse('index'))