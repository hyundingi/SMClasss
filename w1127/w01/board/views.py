from django.shortcuts import render,redirect
from board.models import Board
from member.models import Member

# Create your views here.
def blist(request):
  qs = Board.objects.all()
  context = {'board':qs}
  return render(request, 'blist.html', context)

def bwrite(request):
  # 글쓰기 페이지 열기
  if request.method == 'GET':
    return render(request, 'bwrite.html')
  
  # 쓴 게시글 저장
  else:
    id = request.session['session_id']
    nicName = request.session['session_nicName']
    member = Member.objects.get(id=id)
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    bfile = request.FILES.get('bfile','')

    qs = Board.objects.create(member=member, btitle=btitle, bcontent=bcontent, bfile=bfile)
    qs.bgroup = qs.bno
    qs.save()
    return redirect('/board/blist/')
    # return render(request, 'bwrite.html')

def bview(request, bno):
  # 클릭한 게시글 내용 가져오기
  qs = Board.objects.filter(bno=bno)
  # 이전글
  prev_qs = Board.objects.filter()
  context = {'board':qs[0]}
  return render(request, 'bview.html', context)

