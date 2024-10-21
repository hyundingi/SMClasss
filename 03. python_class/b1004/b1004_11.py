students = []
s_title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']


no = 1
# 학생성적프로그램
while True:
  print("[학생성적프로그램]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 학생등수조회")
  print("0. 프로그램 종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요. >> ")

  if choice == '1':
    while True:
      name = input(f"[뒤로가기: 0] {no}번째 학생 이름 : ")
      if name == '0':
        print("메뉴 화면으로 이동합니다.")
        break
      kor = int(input("국어 점수 : "))
      eng = int(input("국어 점수 : "))
      math = int(input("국어 점수 : "))
      total = kor+eng+math
      avg = total/3
      rank = 0

      s = [no, name, kor, eng, math, total, avg, rank]
      students.append(s)
      no += 1

  elif choice == '2':
    for st in s_title:
      print(st, end='\t')
    print()
    print('-'*60)
    for s in students:
      print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\t")
      print()
    
  elif choice == '3':
    print("[학생성적수정]")
    print()
    while True:
      name = input("[뒤로가기: 0] 수정하고자 하는 학생이름을 입력하세요. >> ")
      if name == '0':
        break

      for s in students:
        count = 0
        if s[1] == name:
          print(f"{name} 학생을 찾았습니다.")
          print("[과목선택]")
          print("-"*60)
          print("1. 국어 점수")
          print("2. 영어 점수")
          print("3. 수학 점수")
          choice = int(input("원하는 번호 입력 : "))

          if choice == 1:
            print(f'현재 국어 점수는 {s[2]}점 입니다.')
            s[2] = int(input('변경된 점수 입력 : '))
            
          elif choice == 2:
            print(f'현재 영어 점수는 {s[3]}점 입니다.')
            s[3] = int(input('변경된 점수 입력 : '))

          elif choice == 3:
            print(f'현재 수학 점수는 {s[4]}점 입니다.')
            s[4] = int(input('변경된 점수 입력 : '))
          
          s[5] = s[2]+s[3]+s[4] # 합계 변경
          s[6] = s[5]/3         # 평균 변경
          print(f'{name} 학생의 성적이 변경되었습니다.')
          count = 1
          break
      if count == 0:
        print('수정하고자 하는 학생이름이 없습니다.')
        print()

  elif choice == '4':
    while True: 
      print("[학생성적검색]")
      print()
      name = input("[뒤로가기: 0] 찾고자 하는 학생이름을 입력하세요. >> ")
      if name == '0':
        break

      count = 0
      for s in students:
        if s[1] == name:
          print(f"{name} 학생을 찾았습니다.")

          # 찾은 학생의 데이터 출력
          for st in s_title:
            print(st, end='\t')
          print()
          print('-'*60)
          print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\t")
          print()
          count = 1
          break
        
      if count == 0:
        print("찾고자하는 이름이 없습니다.")
        print()
        

  elif choice == '5':
    print("[학생성적삭제]")
    print()
    count = 0
    while True:
      name  = input('[뒤로가기: 0] 삭제할 학생 이름을 입력하세요. >> ')
      for s in students:
        if name == s[1]:
          print(f'{s[1]} 학생의 정보를 삭제합니다.')
          students.remove(s)
          count = 1
      if count == 0:
        print('찾고자 하는 학생이 없습니다.')
      if name == '0':
        print('메뉴 화면으로 돌아갑니다.')
        break
     
  elif choice == '6':
    print("[학생등수조회]")
    print()
    
    for ra in students:
     pass

  elif choice == '0':
    print("프로그램을 종료합니다.")
    break
