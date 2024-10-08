students = [
  {'no':1,'name': "홍길동",'kor':100,'eng':100,'math':99,'total':299,'avg':99.67,'rank':0},
  {'no':2,'name': "유관순",'kor':80,'eng':80,'math':85,'total':245,'avg':81.67,'rank':0},
  {'no':3,'name': "이순신",'kor':90,'eng':90,'math':91,'total':271,'avg':90.33,'rank':0},
  {'no':4,'name': "강감찬",'kor':60,'eng':65,'math':67,'total':192,'avg':64.00,'rank':0},
  {'no':5,'name': "김구",'kor':100,'eng':100,'math':84,'total':284,'avg':94.67,'rank':0},
]

s_title = ['번호', '이름','국어','영어','수학','합계','평균','등수']
choice = 0
check = 0 # 체크변수
stuNo = len(students) # 리스트에 학생이 있으면 그 인원수로 변경
no = 0; name = ""; kor = 0; eng = 0; math = 0; total = 0; avg = 0; rank = 0    # 성적처리변수
count = 1 # 성적 처리 


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
      print("[학생성적입력]")

      # 학생성적 직접입력
      no = stuNo + 1 # 리스트 - 학생수
      name = input(f"[프로그램 종료 '0' 입력] {no}번재 학생의 이름을 입력하세요. >> ")
      if name == '0':
        print("첫화면으로 돌아갑니다.")
        print()
        break
      kor = int(input("국어 점수를 입력하세요. >> "))
      eng = int(input("영어 점수를 입력하세요. >> "))
      math = int(input("수학 점수를 입력하세요. >> "))
      total = kor+eng+math
      avg = total/3
      ss = {
        'no':no, 'name':name, 'kor':kor, 'eng':eng, 'math':math, 'total':total, 'avg':avg, 'rank':rank
      }
      students.append(ss)
      stuNo += 1 # 학생 수 증가
      print()
      print(f"{name} 학생의 성적이 저장되었습니다.")

  elif choice == '2':
    print()
    print('                      [학생성적출력]')
    print('순번\t이름\t국어\t영어\t수학\t합계\t평균\t등수\t')
    print('-'*60)
    for i in students:
      print(f'{i['no']}\t{i['name']}\t{i['kor']}\t{i['eng']}\t{i['math']}\t{i['total']}\t{i['avg']}\t{i['rank']}\t')
    print()

  elif choice == '3':
    print("[학생성적수정]")
    print()
    re_name = input('수정할 학생의 이름을 입력하세요. >> ')
    for re in students:
      if re_name == re['name']:
        print(re_name, '학생을 찾았습니다.')

  elif choice == '4':
    print("[학생성적검색]")
  elif choice == '5':
    print("[학생성적삭제]")
  elif choice == '6':
    print("[등수처리]")

  elif choice == '7':
    while True:
      print('[학생성적정렬]')
      print('1. 이름 순차정렬')
      print('2. 이름 역순정렬')
      print('3. 합계 순차정렬')
      print('4. 합계 역순정렬')
      print('5. 번호 순차정렬')
      print('0. 이전페이지로 이동')
      print('-'*50)
      choice = input('원하는 번호를 입력하세요. >> ')

      if choice == '1':
        students.sort(key=lambda x:x['name'])
      elif choice == '2':
        students.sort(key=lambda x:x['name'], reverse=True)
      elif choice == '3':
        students.sort(key=lambda x:x['total'])
      elif choice == '0':
        print('이전페이지로 이동합니다.')
        break
      print('정렬이 완료되었습니다.')
      print()







# 학생성적입력부분을 구현하시오
# dict 타입으로 입력할것
# 번호, 이름, 국어, 영어, 수학, 합계, 평균 , 등수
# 입력이 완료되면 출력이 바로 되도록 하시오


