from django.shortcuts import render, redirect
from board.models import Board
from django.db.models import Max
from django.contrib import messages
from django.db.models import F

# Create your views here.

# 게시글 리스트
def blist(request):
  qs = Board.objects.all().order_by('-bgroup', 'bstep')
  context = {'blist':qs}
  return render(request, 'blist.html', context)

# 글쓰기 페이지, 글쓰기 저장
def bwrite(request):
  if request.method == 'GET':
    return render(request, 'bwrite.html')
  else:
    id = request.POST.get('id')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    # no = Board.objects.aggregate(max_bno = Max('bno'))
    # no['max_bno']+1

    # bno, date : 자동
    # bstep, bindent, bhit = default 0
    # id, btitle, bcontent - 입력받음
    # bgroup - 차후 입력

    # 오라클 sequence.nextval, sequence.currval :: 여기서 기능 사용할 수 없음
    qs = Board.objects.create(id=id, btitle=btitle, bcontent=bcontent)
    qs.bgroup = qs.bno
    qs.save()
    messages.success(request, message = '게시글이 저장되었습니다.')

    # return redirect('/board/blist/')
    return render(request, 'bwrite.html', {'w_msg':'게시글이 저장되었습니다.'})
  

# 게시글 상세보기
def bview(request, bno):
  
  # filter 로 조회수 올리기
  # qs = Board.objects.filter(bno=bno)
  qs = Board.objects.filter(bno=bno)
  qs.update(bhit=F('bhit')+1)
  context = {'board':qs[0]}

  # get으로 조회수 올리기
  # qs = Board.objects.get(bno=bno)
  # qs.bhit += 1
  # qs.save()
  # context = {'board':qs}

  return render(request, 'bview.html', context)


# 게시글 수정
def bmodify(request, bno):
  if request.method == 'GET':
    qs = Board.objects.filter(bno=bno)
    context = {'board':qs[0]}
    return render(request, 'bmodify.html', context)
  else:
    bno = request.POST.get('bno')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    qs = Board.objects.get(bno=bno)
    qs.btitle = btitle
    qs.bcontent = bcontent
    qs.save()
    # return redirect('board:blist')
    return render(request, 'bmodify.html', {'u_msg':bno})
  

def bdelete(request, bno):
  Board.objects.get(bno=bno).delete()
  return render(request, 'blist.html', {'d_msg':bno})

def breply(request, bno):
  if request.method == 'GET':
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request, 'breply.html', context)
  else:
    bgroup = int(request.POST.get('bgroup'))  # type : str > int
    bstep = int(request.POST.get('bstep'))
    bindent = int(request.POST.get('bindent'))
    id = request.POST.get('id')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')

    ## 다른 답변달기에 bstep을 1씩 증가
    qs = Board.objects.filter(bgroup = bgroup, bstep__gt=bstep)
    qs.update(bstep = F('bstep')+1)
    
    # db저장
    # bgroup 부모의 그룹을 입력
    Board.objects.create(id=id, btitle=btitle, bcontent=bcontent, bgroup=bgroup, bstep=bstep+1, bindent=bindent+1)

    # return redirect('board:blist')
    return render(request, 'blist.html', {'r_msg':'1'})


