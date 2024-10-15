# students 리스트 타입
students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
choice = 0 # 전역변수
chk = 0    # 체크변수
count = 1  # 성적처리
stuNo = len(students)  # 리스트에 학생이 있으면, 그 인원으로 변경
no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0 #성적처리변수

# ------- 함수선언 ----------

# ---------------------------
# ---------------------------
# ---------------------------
# ---------------------------
# ---------------------------
# ---------------------------

while True:
  print("[ 학생성적프로그램 ]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("7. 학생성적정렬")
  print("0. 프로그램 종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요.(0.종료)>> ")

  if choice == '1':
    while True:
      print()
      print('[학생성적입력]')
      name = input('학생 이름 입력 (0. 뒤로가기) >> ')
      if name == '0':
        print('메인화면으로 돌아갑니다.')
        break
      
      score = []
      for i in range(3):
        sub = int(input(f'{s_title[i+2]} 점수 : '))
        total += sub
        avg = total/3
        score.append(sub)
      score.append(total)
      score.append(avg)
      stuNo += 1
      no = stuNo
      
      ss = {'no':no, 'name':name, 'kor':score[0],'eng':score[1],'math':score[2],'total':score[3],'avg':score[4], 'rank':0}
      students.append(ss)

  elif choice == '2':
    print()
    print('[학생성적출력]')
    for i in s_title:
      print(i, end = '\t')
    print()
    print('-'*60)
    for s in students:
      k = s.keys()
      k = list(k)
      print()
      for ss in range(len(k)):
        print(s[k[ss]], end='\t')
      print()
  elif choice == '3':
    while True:
      print()
      print('[학생성적수정]')
      name = input('성적 수정할 학생 이름을 입력하세요. (0. 뒤로가기) >> ')
      if name == '0':
        break
      for i in students:
        if name == i['name']:
          print('수정 항목 선택')
          print('1. 국어 성적')
          print('2. 영어 성적')
          print('3. 수학 성적')
          choice = input('수정 항목을 선택하세요. >> ')
          if choice == '1':
            print(f'현재 국어 점수 : {i['kor']}')
            i['kor'] = int(input('변경된 점수 입력 : '))
          elif choice == '2':
            print(f'현재 영어 점수 : {i['eng']}')
            i['eng'] = int(input('변경된 점수 입력 : '))
          elif choice == '3':
            print(f'현재 수학 점수 : {i['math']}')
            i['math'] = int(input('변경된 점수 입력 : '))
          i['total'] = i['kor']+i['eng']+i['math']
          i['avg'] = i['total']/3
      if name != i['name']:
        print('찾으시는 학생이 없습니다. 다시 입력하세요.')

  elif choice == '4':
    print()
    print('[학생성적검색]')
    name = input('검색하려는 학생 이름 ')
  elif choice == '5':
    print()
    print('[학생성적삭제]')
  elif choice == '6':
    print()
    print('[학생등수처리]')