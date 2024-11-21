from django.shortcuts import render, redirect
from member.models import Member

# Create your views here.
def login(request):
  if request.method == 'GET':
    return render(request, 'login.html')
  else:
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    qs = Member.objects.filter(id=id, pw=pw)
    if qs:
      ## 세션 연결
      request.session['session_id'] = id
      request.session['session_nicname'] = qs[0].nicname
      msg = '1'
    else:
      msg = '0'
    return render(request, 'login.html', {'msg':msg})
    

def logout(request):
  request.session.clear()
  return redirect('/')


def join01(request):
  return render(request, 'join01.html')