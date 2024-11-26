from django.shortcuts import render, redirect
from board.models import Board
from member.models import Member
from django.db.models import F
from datetime import datetime
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
# 게시판 리스트 
def blist(request):
  npage = int(request.GET.get('npage',1)) # 현재페이지 가져오기 없으면 1페이지
  qs = Board.objects.all().order_by('-bgroup', 'bstep')
  # 하단 페이지 처리 (넘버링)
  paginator = Paginator(qs,10)
  blist = paginator.get_page(npage) # 1페이지 10개
  context = {'blist': blist, 'npage':npage}
  return render(request, 'blist.html', context)

# 글쓰기 페이지 열기 , 글쓰기 board에 저장
def bwrite(request):
  if request.method == 'GET':
    return render(request, 'bwrite.html')
  else:
    # 자동입력 : bno, bgroup, bstep, bindent, bdate
    # 가져와야 하는 것 : btitle, bcontent

    nicName = request.session.get('session_nicName')  # 섹션 닉네임의 닉네임 값을 받아옴
    member = Member.objects.get(nicName=nicName)
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    bfile = request.FILES.get('bfile','')
    print('파일이름 : ', request.FILES)

    # db 저장 - AutoField 번호 생성 > bgroup에도 같이 저장
    qs = Board.objects.create(member=member, btitle=btitle, bcontent=bcontent, bfile=bfile)
    qs.bgroup = qs.bno
    qs.save()

    context = {'wmsg':'1'}
    return render(request, 'bwrite.html', context)


# 글 상세보기 / 조회수 증가 (조회수 새로고침 x)
def bview(request, bno):
  # [조회수] get 방식
  # qs = Board.objects.get(bno=bno)
  # qs.bhit += 1
  # qs.save()

  # [조회수] filter 방식 - update() 명령어가 존재
  # F함수 - 필드 값을 참조
  qs = Board.objects.filter(bno=bno)
  # 이전글
  prev_qs = Board.objects.filter(Q(bgroup__lt=qs[0].bgroup,bstep__lte=qs[0].bstep) | Q(bgroup=qs[0].bgroup,bstep__gt=qs[0].bstep)).order_by("-bgroup","bstep").first()
  # 다음글
  next_qs = Board.objects.filter(Q(bgroup__gt=qs[0].bgroup,bstep__gte=qs[0].bstep) | Q(bgroup=qs[0].bgroup,bstep__lt=qs[0].bstep)).order_by("-bgroup","bstep").last()

  npage = request.GET.get('npage',1) # 현재페이지 가져오기 없으면 1페이지

  context = {'board':qs[0], 'prev':prev_qs, 'next':next_qs, 'npage':npage}
  response = render(request, 'bview.html', context)

  # 쿠키 사용 기간 - 1일
  # 11월 25일 23시 59분 0초로 셋팅됨
  tomorrow = datetime.replace(datetime.now(), hour=23, minute=59, second=0)
  # 쿠키 설정 포맷 - strftime: 시간 포맷 형태
  expires = datetime.strftime(tomorrow, '%a,%d-%b-%Y %H:%M:%S GMT')


  # 조회수를 증가하면 cookie_name에 증가한 번호 추가
  # cookie_name 존재하면 
  print('cookie_name : ', request.COOKIES.get('cookie_name'))
  if request.COOKIES.get('cookie_name') is not None:
    # 쿠키를 읽어와서 안에 1|3|4 > 2:1증가 3:증가안됨
    cookies = request.COOKIES.get('cookie_name')
    cookies_list = cookies.split('|')
    response = render(request, 'bview.html', context)
    if str(bno) not in cookies_list:
      # 안에 1|3|4|2
      # 번호가 없으면 번호를 추가 
      response.set_cookie('cookie_name', cookies+f'|{bno}', expires=expires)
      qs.update(bhit = F('bhit')+1)
    else:
      pass
  else: # cookie_name 존재하지 않으면
    response.set_cookie('cookie_name', bno, expires=expires)
    qs.update(bhit = F('bhit') + 1 )

  return response

# 글 삭제
def bdelete(request, bno):
  qs = Board.objects.get(bno=bno)
  qs.delete()
  context = {'dmsg':bno}
  return render(request, 'blist.html', context)

def bupdate(request, bno):
  if request.method == 'GET':
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request, 'bupdate.html', context)
  else:
    bno = request.POST.get('bno')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    bfile = request.FILES.get('bfile','')
    qs = Board.objects.get(bno=bno)
    qs.btitle = btitle
    qs.bcontent = bcontent
    
    if bfile:
      qs.bfile = bfile
    qs.save()
    return redirect('board:bview', bno)

# 답글달기
def breply(request, bno):
  if request.method == 'GET':
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request, 'breply.html', context)
  else:
    id = request.POST.get('id') 
    member = Member.objects.get(id=id)
    bgroup = int(request.POST.get('bgroup'))  # 답글들 그룹핑
    bstep = int(request.POST.get('bstep'))    # 답글의 순서
    bindent = int(request.POST.get('bindent'))# 들여쓰기
    btitle = request.POST.get('btitle')  # 들여쓰기
    bcontent = request.POST.get('bcontent') # 들여쓰기

    # 같은 bgroup에서 bstep이 더 큰 것만 검색해서, 값 1씩 증가
    qs = Board.objects.filter(bgroup=bgroup, bstep__gt=bstep)
    qs.update(bstep = F('bstep')+1)

    qs = Board(member=member, btitle=btitle, bcontent=bcontent, bgroup=bgroup, bstep=bstep+1, bindent=bindent+1)
    qs.save()
    context = {'rmsg':'1'}
    return render(request, 'breply.html', context)