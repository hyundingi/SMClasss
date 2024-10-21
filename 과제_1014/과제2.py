# 2. students 파이썬 구현
# b1004 > 학생성적프로그램 
# 리스트를 딕셔너리로 바꿔서 구현
# 1008 9번 참조

students = []
s_title = ['번호', '이름','국어','영어','수학','합계','평균','등수']

no = 0

# 학생성적프로그램 메인
while True:
  print("[학생성적프로그램]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 학생등수조회")
  print('7. 학생성적정렬')
  print("0. 프로그램 종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요. >> ")

  if choice == 0:
    print('프로그램을 종료합니다.')
    break

  elif choice == '1':
    while True:
      print()
      print('[학생성적입력]')
      no += 1
      name = input('[뒤로가기 0 입력] 학생 이름을 입력하세요. >> ')
      if name == '0':
        print('처음화면으로 돌아갑니다.')
        break
      kor = int(input('국어점수를 입력하세요. >> '))
      eng = int(input('영어점수를 입력하세요. >> '))
      math = int(input('수학점수를 입력하세요. >> '))
      total = kor+eng+math
      avg = round(total/3,2)
      rank = 0
      inputstu = {'no':no, 'name':name, 'kor':kor, 'eng':eng, 'math':math, 'total':total, 'avg':avg, 'rank':rank}
      students.append(inputstu)
  
  elif choice == '2':
    print()
    print('[학생성적출력]')
    for i in s_title:
      print(i, end='\t')
    print()
    print('-'*60)
    for s in students:
      for key in s:
       print(s[key], end='\t')
      print()

  elif choice == '3':
    print()
    print('[학생성적수정]')
    searchstu = input('[뒤로가기 0 입력] 수정할 학생의 이름을 입력하세요. >> ')
    if searchstu == '0':
      print('메인 화면으로 돌아갑니다.')
      break
    for search in students:
        if searchstu == search['name']:
          print(f'{searchstu}학생을 찾았습니다.')
          print()
          print('[수정항목선택]')
          print('-'*60)
          print('1. 국어점수')
          print('2. 영어점수')
          print('3. 수학점수')
          print('-'*60)
          choice = input('원하는 항목을 선택하세요. >> ')
          if choice == '1':
            print(f'기존 점수 : {search['kor']}')
            search['kor'] = int(input('수정 점수 : '))
          if choice == '2':
            print(f'기존 점수 : {search['eng']}')
            search['eng'] = int(input('수정 점수 : '))
          if choice == '3':
            print(f'기존 점수 : {search['math']}')
            search['math'] = int(input('수정 점수 : '))
          search['total'] = search['kor'] + search['eng'] + search['math']
          search['avg'] = round(search['total']/3,2)
        elif searchstu != search['name']:
          print('찾는 학생이 없습니다. 다시 입력하세요. >> ')

  elif choice == '4':
    while True:
      print()
      print('[학생성적검색]')
      searchstu = input('[뒤로가기 0 입력] 찾을 학생의 이름을 입력하세요. >> ')
      if searchstu == '0':
        print('메인 화면으로 돌아갑니다.')
        break
      for search in students:
        if searchstu == search['name']:
          print(f'{searchstu}학생을 찾았습니다.')
          print()
          for i in s_title:
            print(i, end='\t')
          print()
          print('-'*60)
          for key in search:
            print(search[key], end='\t')
        elif searchstu != search['name']:
          print(f'{searchstu}학생을 찾지 못했습니다. 다시 입력해주세요.')

  elif choice == '5':
    while True:
      print()
      print('[학생성적삭제]')
      searchstu = input('[뒤로가기 0 입력] 삭제할 학생의 이름을 입력하세요. >> ')
      if searchstu == '0':
          print('메인 화면으로 돌아갑니다.')
          break
      for idx, search in enumerate(students):
        if searchstu == search['name']:
          print(f'{searchstu}학생을 찾았습니다.')
          print()
          delinput = input('정말로 삭제하시겠습니까? \n예 - 1 / 아니요 - 2 >> ')
          if delinput == '1':
            del students[idx] 
            print(f'{searchstu}학생을 삭제했습니다.')
          elif delinput == '2':
            break
        elif searchstu != search['name']:
          print('찾으시는 학생이 없습니다. 다시 입력하세요.')

  elif choice == '6':
    print()
    print('[등수처리]')
    for s in students:
      count = 1
      for ss in students:
        if s['total'] < ss['total']:
          count += 1
      s['rank'] = count

   

    
  elif choice == '7':
    print()
    print('[학생성적정렬]')
    print('-'*60)
    print('[정렬방식선택]')
    print('1. 이름 순차정렬')
    print('2. 이름 역순정렬')
    print('3. 합계 순차정렬')
    print('4. 합계 역순정렬')
    print('5. 번호 순차정렬')
    print('0. 이전페이지로 이동')
    print('-'*60)
    choice = input('원하시는 번호를 입력하세요. >> ')

    if choice == '1':
      students.sort(key=lambda x:x['name'])
    if choice == '2':
      students.sort(key=lambda x:x['name'], reverse=True)
    if choice == '3':
      students.sort(key=lambda x:x['total'])
    if choice == '4':
      students.sort(key=lambda x:x['total'], reverse=True)
    if choice == '5':
      students.sort(key=lambda x:x['no'])
    if choice == '0':
      print('메인화면으로 돌아갑니다.')
      break

