from django.shortcuts import render, redirect
from member.models import Member

# Create your views here.
def login(request):
  # 로그인 창 열기
  if request.method == 'GET':
    return render(request, 'login.html')
  # 로그인 데이터 넘기기
  else:
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    qs = Member.objects.filter(id=id, pw=pw)
    if qs:
      msg = '0'
      request.session['session_id'] = qs[0].id
      request.session['session_nicName'] = qs[0].nicName
    else:
      msg = '1'
    context = {'msg':msg}
    return render(request, 'login.html', context)
  
def logout(request):
  request.session.clear()
  return redirect('/')