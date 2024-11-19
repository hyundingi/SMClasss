from django.shortcuts import render, redirect
from students.models import Student
from django.urls import reverse

# Create your views here.

# 학생 입력 페이지 호출(get) / 학생 저장(post)
def write(request):
  if request.method == 'GET':
    return render(request, 'write.html')
  else: # post
    name = request.POST.get('name')  ## 데이터가 없을 시 None으로 데이터를 넘겨줌
    major = request.POST['major']    ## 데이터가 없을 시 error
    grade = request.POST.get('grade')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    # hobby = request.POST.get('hobby')        # 여러개 선택해도 한개만 가져옴
    hobbys = request.POST.getlist('hobby')     # [체크박스 데이터 가져오기] 리스트 타입으로 가져와야함
    # hobby = ','.join(hobbys)                 # 스트링 타입으로 변경
    # hobby_list = hobby.split(',')            # 다시 리스트 타입으로 변경

    ## qs.save
    qs = Student(name=name, major=major, grade=grade, age=age, gender=gender, hobby=hobbys)
    qs.save()

    # qs.save 없이 바로 저장 -- create
    # Student.objects.create(name=name, major=major, grade=grade, gender=gender, hobby=hobbys)

    return redirect('/students/list/')
  

# 학생 리스트
def list(request):
  ## 학생 전체 정보 가져오기
  qs = Student.objects.all()
  context = {'slist':qs}
  return render(request, 'list.html', context)

# 학생상세보기
def view(request, name):
  qs = Student.objects.get(name=name)
  context = {'stu':qs}
  return render(request, 'view.html', context)

# 학생정보수정페이지 , 학생 수정 저장
def update(request):
  if request.method == 'GET':
    name = request.GET['name']
    print(name)
    qs = Student.objects.get(name=name)
    context = {'stu':qs}
    return render(request, 'update.html', context)
  else:  # post 형태
    name = request.POST.get('name')
    major = request.POST.get('major')
    grade = request.POST.get('grade')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    hobbys = request.POST.getlist('hobby')

    # stu 검색 후 값 업데이트
    qs = Student.objects.get(name=name)
    qs.major = major
    qs.grade = grade
    qs.age = age
    qs.gender = gender
    qs.hobby = hobbys
    qs.save()
    # 약식
    return redirect('students:view', name)
    # 정규식
    # return redirect(reverse('students:view', args=(name, )))


# 학생정보삭제
def delete(request, name):
  qs = Student.objects.get(name=name)
  qs.delete()
  # Student.objects.delete(name=name)
  # Student.objects.get(name=name).delete()

  return redirect('students:list')

# 학생검색
def search(request):
  search = request.GET.get('search')
  print('검색 단어 : ', search)

  ## 데이터 검색
  qs = Student.objects.filter(name__contains=search)
  context = {'slist':qs}
  return render(request, 'list.html', context)