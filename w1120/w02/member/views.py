from django.shortcuts import render, redirect
from member.models import Member

# Create your views here.
def login(request):
  if request.method == 'GET':
    response = render(request, 'login.html')
  else:
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    qs = Member.objects.filter(id=id, pw=pw)   
    if qs:
      emsg = ''
      context = {'emsg':emsg, 'member':qs[0]}
      request.session['session_id'] = id
      request.session['session_nicName'] = qs[0].nicName
      response = render(request, 'index.html', context)
    else:
      emsg = '아이디 또는 패스워드가 일치하지 않습니다.'
      context = {'emsg':emsg, 'member':''}
      response =  render(request, 'login.html', context)
  return response

def logout(request):
  # 섹션모두삭제
  request.session.clear()
  # 섹션하나삭제
  # del request.session['session_id'] 
  return redirect('index')

def mlist(request):
  return render(request, 'mlist.html')

def cookWrite(request):
  response = render(request, 'cookWrite.html')
  if request.method == 'GET':
    print('get 방식으로 들어옴')
  else:
    response = render(request, 'index.html')
    print('post 방식으로 들어옴')
    ckey = request.POST.get('ckey')
    cvalue = request.POST.get('cvalue')
    response.set_cookie(ckey, cvalue)
  
  return response

def cookDelete(request):
  if request.method == 'GET':
    response = render(request, 'cookDelete.html')
  else:
    response = render(request, 'index.html')
    c = request.POST.get('ckey')
    response.delete_cookie(c)
    print(c, '쿠기가 삭제되었습니다.')
  return response