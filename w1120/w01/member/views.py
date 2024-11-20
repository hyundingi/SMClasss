from django.shortcuts import render
from member.models import Member


# Create your views here.

# 회원전체리스트 페이지
def mlist(request):
  qs = Member.objects.all()
  context = {'mlist':qs}
  return render(request, 'mlist.html', context)

# 로그인 페이지
def login(request):
  # 쿠키 정보 전체 보기   request.COOKIES
  # 쿠키 정보 검색        request.COOKIES.get('쿠키이름')
  # 쿠키 저장             response.set_cookie('key', 'value')
  # 쿠키 삭제 :           response.delete_cookie('key')


  if request.method == 'GET':
    print('쿠키정보 : ',request.COOKIES)
    print('쿠키정보 : ',request.COOKIES.get('cookinfo'))
    saveId = request.COOKIES.get('saveId','')
    context = {'saveId': saveId}
    response = render(request, 'login.html', context)

    if request.COOKIES.get('cookinfo'):
      # max_age = 60초 *60분 (1시간)| 60초 * 60분 * 24시간 * 30일 (1달)/ max_age 가 없으면 브라우저 종료시 삭제
      response.set_cookie('cookinfo', '1111', max_age=60*60) 
    return response
  else:
    print('쿠키정보 : ', request.COOKIES)
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    # pw = request.POST['pw'] 같은 경우 값이 없으면  에러남
    saveId = request.POST.get('saveId', '값 없음')
    print('전달받은 정보 : ', id,pw,saveId)
    response = render(request, 'login.html')

    ## 아이디기억하기 정보가 있으면
    if saveId is not None:
      response.set_cookie('saveId',id, max_age=60*60) # 아이디 기억하기 : 체크가 있으면 쿠키 저장
    else:
      response.delete_cookie('saveId') # 아이디 기억하기 : 체크가 없으면 삭제

    return response
  
def login2(request):
  if request.method == 'GET':
    cookId = request.COOKIES.get('cookId', '')
    context = {'cookId':cookId}
    return render(request, 'login2.html', context)
  
  else:  # post 방식 (로그인 버튼 클릭했을 때)
    response = render(request, 'index.html')
    # 3개의 정보 받아오기
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    saveId= request.POST.get('saveId')

    # 아이디 저장을 선택 했냐 안 했냐
    if saveId is not None:
      # 햇으면 쿠키에 아이디 저장
      response.set_cookie('cookId', id, max_age=60*60)
    else:
      # 안 햇으면 쿠키 삭제
      response.delete_cookie('cookId')

    return response
  

def product(request):
  if request.method == 'GET':
    saveId = request.COOKIES.get('saveId','')
    saveName = request.COOKIES.get('saveName','')
    context = {'saveId':saveId , 'saveName':saveName}
    return render(request, 'product.html', context)
  else:
    response = render(request, 'index.html')
    pId = request.POST.get('pId')
    pName = request.POST.get('pName')
    saveProduct = request.POST.get('saveProduct')

    if saveProduct is not None:
      response.set_cookie('saveId', pId, max_age=60*60)
      response.set_cookie('saveName', pName, max_age=60*60)
    else:
      response.delete_cookie('saveId')
      response.delete_cookie('saveName')
  
  return response


def m2(request):
  if request.method == 'GET':
    saveId = request.COOKIES.get('saveId', '')
    saveM = request.COOKIES.get('saveM', '')
    saveO = request.COOKIES.get('saveO', '')
    context = {'saveId':saveId, 'saveM':saveM, 'saveO':saveO}
    return render(request, 'm2.html', context)
  else:
    response = render(request, 'index.html')
    id = request.POST.get('memberId')
    money = request.POST.get('money')
    option = request.POST.get('option')
    save = request.POST.get('saveMember')

    if save is not None:
      response.set_cookie('saveId', id, max_age=60*60)
      response.set_cookie('saveM', money, max_age=60*60)
      response.set_cookie('saveO', option, max_age=60*60)
    else:
      response.delete_cookie('saveId')
      response.delete_cookie('saveM')
      response.delete_cookie('saveO')
      
  return response
