from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from member.models import Member
from django.core import serializers

# Create your views here.
# 로그인
def login(request):
  return render(request, 'login.html')

# adjx 통신
# csrf_token
@csrf_exempt #csrf_tokem #예외처리
def loginChk(request):
  id = request.POST.get('id','')
  pw = request.POST.get('pw','')
  print('html에서 넘어온 데이터 : ', id, pw)
  # 변수 보내는 방법
  # qs = Member.objects.filter(id=id, pw=pw)
  # if qs:
  #   context = {'id':qs[0].id, 'nicName':qs[0].nicName, 'result':'success'}
  # else:
  #   context = {'result':'fail'}
  # return JsonResponse(context)

  # 객체 보내는 방법(filter 타입) - list 타입으로 보내야함 (타입에러발생)
  qs = list(Member.objects.filter(id=id, pw=pw).values())
  json_qs = serializers.serialize('json',qs)
  if qs:
    context = {'member':qs, 'result':'success'}
  else:
    context = {'result':'fail'}
  return JsonResponse(context)

  # 객체 보내는 방법 (get타입) --- 안 됨...
  # qs = Member.objects.get(id=id, pw=pw)
  # if qs:
  #   context = {'member':qs, 'result':'success'}
  # else:
  #   context = {'result':'fail'}
  # return JsonResponse(context)

def join01(request):
  return render(request, 'join01.html')

def join02(request):
  return render(request, 'join02.html')

# ajax 통신
def idChk(request):
  id = request.POST.get('id','')
  print(id)
  context = {'id':id}
  return JsonResponse(context)

def join03(request):
  return render(request, 'join03.html')