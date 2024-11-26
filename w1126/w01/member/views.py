from django.shortcuts import render, redirect
from member.models import Member

# Create your views here.
# 로그인 페이지 열기 > 로그인 성공/실패
def login(request):
  if request.method == 'GET':
    return render(request, 'login.html')
  else:
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    qs = Member.objects.filter(id=id, pw=pw)
    # 정상 로그인 됐을 경우
    if qs:
      request.session['session_id'] = qs[0].id
      request.session['session_nicName'] = qs[0].nicName
      context = {'lmsg':'1'}
    # 아이디 혹은 비밀번호가 틀렸을 경우
    else:
      context = {'lmsg':'0'}

    return render(request, 'login.html', context)

# 로그아웃
def logout(request):
  request.session.clear()
  return redirect('/')