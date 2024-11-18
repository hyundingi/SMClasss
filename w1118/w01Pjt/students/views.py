from django.shortcuts import render, redirect
from students.models import Student

# Create your views here.

# 학생 입력 페이지 호출 - 페이지를 보여줄 때(render) / 학생 입력 admin 저장, 입력 등 (redirect)
def write(request):
  # render - html 파일 호출
  if request.method == 'GET':
    print('GET 방식으로 들어옴')
    return render(request, 'write.html')

# 학생 입력 저장
  else:
    print('POST방식으로 들어옴')
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    print('입력값 : ', name, major, grade, age, gender)

    # db에 저장
    Student.objects.create(name=name, major=major, grade=grade, age=age, gender=gender)
    print('학생 1명 저장')

  return redirect('students:list')
  # return redirect('/students/list')

# 학생 리스트 호출
def list(request):
  qs = Student.objects.all()
  # context : 데이터를 전달하는 변수
  context = {'slist':qs}
  return render(request, 'list.html', context)

# 학생 상세 페이지
def View(request, name):
  print('이름 정보 : ', name)
  # get : 없을 경우 에러 / 없을 경우 구문 리턴
  # qs = Student.objects.get(name=name)
  # qs = get_object_or_404(Student, name=name)

  # 없을 경우 빈 괄호 {} / list 타입으로 넘어감
  qs = Student.objects.filter(name=name)
  context = {'stu':qs[0]}
  return render(request, 'View.html', context)

# 학생수정페이지 (url) 매개변수로 데이터 값을 전달받음
def modify(request, name):
  if request.method == 'GET':
    print('modify 이름 정보 : ', name)
    # 1개 데이터 가져오기
    qs = Student.objects.filter(name=name)
    context = {'stu':qs[0]}
    return render(request, 'modify.html',context)
  else:
    print('POST 호출')
    qs = Student.objects.get(name=name)
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    print('수정 modify 정보 : ', name, major, grade, age, gender)
    # db저장
    major =  qs.major
    qs.grade = grade
    qs.age = age
    qs.gender = gender
    qs.save()
    return redirect('students:list')

# 학생수정페이지 (파라미터)
def modify2(request):
  name = request.GET.get('name')
  print('modify2 이름 정보 : ', name)
  qs = Student.objects.filter(name=name)
  context = {'stu':qs[0]}
  return render(request, 'update.html', context)

# 학생수정페이지 (파라미터 appName) 매개변수로 데이터값을 전달받음
def modify3(request, name):
  print('modify3 이름 정보 : ', name)
  qs = Student.objects.filter(name=name)
  context = {'stu':qs[0]}
  return render(request, 'update.html', context)

# 학생 삭제
def delete(request, name):
  print('삭제정보 : ', name)
  Student.objects.get(name=name).delete()
  return redirect('students:list')