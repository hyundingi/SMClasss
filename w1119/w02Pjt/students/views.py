from django.shortcuts import render, redirect
from students.models import Student

# Create your views here.
def write(request):
  if request.method == 'GET':
    return render(request, 'write.html')
  else:  # post 
    name = request.POST.get('name')
    major = request.POST.get('major')
    grade = request.POST.get('grade')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    hobbys = request.POST.getlist('hobby')
    hobby = ','.join(hobbys)

    Student.objects.create(name=name, major=major, grade=grade, age=age, gender=gender, hobby=hobby)

    return redirect('/students/list/')
  

def list(request):
  qs = Student.objects.all()
  context = {'slist':qs}
  return render(request, 'list.html', context)

def view(request, name):
  qs = Student.objects.get(name=name)
  context = {'stu':qs}
  return render(request, 'view.html', context)

def update(request, name):
  if request.method == 'GET':
    qs = Student.objects.get(name=name)
    context = {'stu':qs}
    return render(request, 'update.html', context)
  else: # post
    name = request.GET['name']
    major = request.POST.get('major')
    grade = request.POST.get('grade')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    hobbys = request.POST.getlist('hobby')
    hobby = ','.join(hobbys)

    qs = Student.objects.get(name=name)
    qs.major = major
    qs.grade = grade
    qs.age = age
    qs.gender = gender
    qs.hobby = hobby
    qs.save()
    
    return redirect('/students/list/')

def delete(request, name):
  qs = Student.objects.get(name=name)
  qs.delete()
  return redirect('/students/list/')
