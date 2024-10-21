# students 리스트 타입
students = [

]
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수

# students.txt 파일 읽기
f = open('C:/workspace/SMClasss/b1016/students.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line:
    break
  sstu = line.strip().split(',')
  for i in range(len(sstu)):
    if i == 1:
      continue
    elif i == 6:
      sstu[6] = float(sstu[6])
    else:
      sstu[i] = int(sstu[i])
  students.append(dict(zip(s_title, sstu)))
#print(students)

# -------------------------------------------------------
stuNo = len(students)  # 리스트에 학생이 있으면, 그 인원으로 변경
choice = 0 # 전역변수

s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
chk = 0    # 체크변수
count = 1  # 성적처리
no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0 #성적처리변수

# 메뉴출력함수 시작
def title_program():
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
  return choice

# --------------------
# 학생성적입력함수 시작 - 일반변수 변경
def stu_input():
  while True:
      global stuNo
      print("[ 학생성적 입력 ]")
      # 학생성적 직접 입력
      no = stuNo + 1  # 리스트 - 학생수
      name = input(f"{no}번째 학생 이름을 입력하세요.(0.이전화면) >>")
      if name == "0":
        print("성적입력을 취소합니다.")
        print()
        break
      kor = int(input("국어점수를 입력하세요."))
      eng = int(input("영어점수를 입력하세요."))
      math = int(input("수학점수를 입력하세요."))
      total = kor+eng+math
      avg = total/3
      rank = 0
      ss = { "no":no,"name":name,"kor":kor,"eng":eng,
             "math":math,"total":total,"avg":avg,"rank":rank }
      students.append(ss)
      stuNo += 1  # 학생수 1증가

      # students.txt 파일 쓰기
      f = open('b1016/students.txt','a',encoding='utf-8')
      data = f'{ss['no']},{ss['name']},{ss['kor']},{ss['eng']},{ss['math']},{ss['total']},{ss['avg']},{ss['rank']}'
      f.write(data)
      f.close()

      print(f"{name} 학생성적이 저장되었습니다.!")
      print()
  return stuNo

# --------------------
# 학생성적출력 함수 선언
def stu_output():
  print("[ 학생성적 출력 ]")
  print()
  # 상단출력
  for st in s_title:
    print(st,end="\t")
  print(); print("-"*60)
  # 학생성적출력
  for s in students:
    print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
  print()

# -----------------------
# 학생성적수정 함수 선언
def stu_update():
  flag = 0
  print("[ 학생성적수정 ]")
  name = input("찾고자 하는 학생의 이름을 입력하세요.")
  
  # 전체 학생과 비교
  for s in students:
    if name == s['name']:
      print(f'{name}학생을 찾았습니다.')
      print()
      print("[ 수정 과목 선택 ]")
      print("1. 국어점수")
      print("2. 영어점수")
      print("3. 수학점수")
      choice = input("원하는 번호를 입력하세요.>> ")
      if choice == '1':
        print(f'현재 국어 점수 : {s['kor']}')
        s['kor'] = int(input('변경 국어 점수 입력 >> '))
      elif choice == '2':
        print(f'현재 영어 점수 : {s['eng']}')
        s['eng'] = int(input('변경 영어 점수 입력 >> '))
      elif choice == '3':
        print(f'현재 수학 점수 : {s['math']}')
        s['math'] = int(input('변경 수학 점수 입력 >> '))
      s['total'] = s['kor']+s['eng']+s['math']
      s['avg'] = s['total']/3

      print(f'{name}학생 성적이 수정되었습니다.')

      # 수정된 학생 성적 출력
      stu_output([s])
      flag = 1
    # 찾는 학생이 없을 때
  if flag == 0:
    print(f'{name}학생이 없습니다. 다시 입력하세요. >> ')
 
# -----------------------
# 학생성적검색 함수 선언 
def stu_select():
  while True:
    flag = 0
    print('[학생성적검색]')
    name = input('검색하려는 이름을 입력하세요. (0. 뒤로가기) >> ')
    if name == '0':
      break
    sArr = []
    for idx, s in enumerate(students):
      if s['name'].find(name) != -1:
        print(f'{name}학생을 찾았습니다.')
        sArr.append(s)
        flag = 1
    if flag == 0:
      print('찾는 학생이 없습니다.')
    else:
      print(f'{name} 이름으로 {len(sArr)}명 검색되었습니다.')
      stu_output(sArr)

# -----------------------
# 학생성적삭제 함수 선언
def stu_delete():
  while True:
    print("[ 학생성적 삭제 ]")
    name = input("찾고자 하는 학생의 이름을 입력하세요. (0. 뒤로가기) >> ")
    flag = 0
    sArr = []
    for idx, s in enumerate(students):
      if s['name'] == name:
        flag = 1
        print(f'{name}학생 성적을 삭제하시겠습니까? (삭제시 복구불가)')
        print('1.삭제 2.취소')
        choice = input("원하는 번호를 입력하세요. >> ")
        if choice == "1":
          sArr.append(s)
          del students[idx]
          print(f'{name}학생 성적이 삭제되었습니다.')
          stu_output(students)
          print('[삭제된 내용]')
          stu_output([s])
        else:
          print('학생성적 삭제가 취소되었습니다.')
          break
    if flag == 0:
      print(f'{name}학생이 없습니다. 다시 입력하세요.')

# -----------------------
# 학생성적정렬 함수 선언  
def stu_rank():
  print("[ 등수처리 ]")
  for s in students:
    count = 1
    for st in students:
      if s['total'] < st['total']:
        count += 1
    s['rank'] = count # 등수입력
  print("등수처리가 완료되었습니다.")
  print()
  stu_output(students)

# -----------------------
# 학생성적정렬 함수 선언  
def stu_sort():
   while True:
      print("[ 학생성적 정렬 ]")
      print("1. 이름 순차정렬")
      print("2. 이름 역순정렬")
      print("3. 합계 순차정렬")
      print("4. 합계 역순정렬")
      print("5. 번호 순차정렬")
      print("0. 이전페이지 이동")
      print("-"*40)
      choice = input("원하는 번호를 입력하세요.>> ")
      if choice == "1":
        # 리스트(students)를 가져와서 딕셔너리 중 '이름'을 가져와서 리턴
        students.sort(key=lambda x:x['name'])   
      elif choice == "2":
        students.sort(key=lambda x:x['name'],reverse=True)
      elif choice == "3":
        students.sort(key=lambda x:x['total'])
      elif choice == "4":
        students.sort(key=lambda x:x['total'],reverse=True)
      elif choice == "5":
        students.sort(key=lambda x:x['no'])
      elif choice == "0":
        print("이전페이지로 이동합니다.")
        break
      print("정렬이 완료되었습니다.")