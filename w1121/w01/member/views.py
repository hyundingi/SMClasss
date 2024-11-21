from django.shortcuts import render, redirect
from member.models import Member

# Create your views here.

# 로그인 페이지 / 로그인 값 전송
def login (request):
  # 로그인 페이지를 열어줄 때 
  if request.method == 'GET':
    return render(request, 'login.html')
  # 로그인 버튼을 눌러서 데이터 가져옴 
  else:
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    qs = Member.objects.filter(id=id, pw=pw)
    if qs:
      msg = '로그인 되었습니다.'
      print(msg)
      ## 세션연결
      request.session['session_id'] = id
      request.session['session_nicname'] = qs[0].nicname
      return redirect('/')
    else:
      msg = '아이디 또는 패스워드가 일치하지 않습니다.'
      print(msg)
      return render(request, 'login.html', {'login_msg':msg})
    
def logout(request):
  # 전체 섹션 삭제
  request.session.clear()   
  ## del request.session['session_id'] #  섹션 하나 삭제
  return redirect('/')

# 회원리스트 
def mlist(request):
  id = request.session['session_id']
  if id =='admin':
    qs = Member.objects.all()
  else:
    qs = Member.objects.filter(id=id)
  context = {'mlist':qs}
  
  return render(request, 'mlist.html', context)

# 회원 상세 정보
def mview(request, id):
  qs = Member.objects.filter(id=id)
  context = {'mem':qs[0]}
  return render(request, 'mview.html', context)

# 회원 정보 수정
def mupdate(request, id):
  if request.method == 'GET':
    qs = Member.objects.filter(id=id)
    context = {'mem':qs[0]}
    return render(request, 'mupdate.html', context)
  else:
    id = request.session['session_id']
    ## 관리자 로그인이면 id를 가져와서 저장
    if id =='admin':
      id = request.POST.get('id')
    pw = request.POST.get('pw')
    name = request.POST.get('name')
    nicname = request.POST.get('nicname')
    tel = request.POST.get('tel')
    gender = request.POST.get('gender')
    hobbys = request.POST.getlist('hobby')
    hobby = ','.join(hobbys)

    qs = Member.objects.get(id=id)
    qs.pw=pw
    qs.name=name
    qs.nicname=nicname
    qs.tel=tel
    qs.gender=gender
    qs.hobby=hobby
    qs.save()
    return redirect('member:mlist')


def mwrite(request):
  if request.method == 'GET':
    return render(request, 'mwrite.html')
  else:
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    name = request.POST.get('name')
    nicname = request.POST.get('nicname')
    tel = request.POST.get('tel')
    gender = request.POST.get('gender')
    hobbys = request.POST.getlist('hobby')
    hobby = ','.join(hobbys)
    qs = Member(id=id, pw=pw,name=name, nicname=nicname,tel=tel,gender=gender,hobby=hobby)
    qs.save()
    return redirect('member:mlist')
  
def mdelete(request, id):
  Member.objects.get(id=id).delete()
  return redirect('member:mlist')