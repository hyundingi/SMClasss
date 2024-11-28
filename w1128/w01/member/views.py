from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from member.models import Member
from django.core import serializers


# Create your views here.
def login(request):
  return render(request, 'login.html')

# json 타입 변경 - list, dict 타입이어야 함
# 로그인 체크
#csrf_ecempt 예외처리
def loginChk(request):
  id = request.POST.get('id','')
  pw = request.POST.get('pw','')
  # qs = Member.objects.get(id=id, pw=pw)    # 없으면 에러
  # json_qs = serializers.serialize('json',[qs])  # json 타입변경 (get 방식으로 가져왔을 때)
  qs = Member.objects.filter(id=id, pw=pw) # 없으면 none
  if qs:
    request.session['session_id'] = id
    request.session['session_nicName'] = qs[0].nicName
    qs_list = list(qs.values())    
    context = {'result':'success', 'member':qs_list}
  else:
    print('실패')
    context = {'result':'fail'}
  return JsonResponse(context)

def logout(request):
  context = {'outmsg':'1'}
  request.session.clear()  # 모두삭제/ 한개만 삭제 : del request.session['session_id']
  return render(request, 'index.html', context)

def step03(request):
  return render(request, 'step03.html')

def idChk(request):
  id = request.POST.get('id')
  qs = Member.objects.filter(id=id)
  qs_list = list(qs.values())
  print(id)
  print(qs)
  if not qs:
    context = {'result':'success', 'member':qs_list}
  else:
    context = {'result':'fail'}
  return JsonResponse(context)