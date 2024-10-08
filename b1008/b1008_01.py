stulist = []
no = 0
rank = 0



while True:
  print("[ 학생성적프로그램 ]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("0. 프로그램 종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요.(0.종료)>> ")

  if choice == '0':
    print('프로그램을 종료합니다.')
    break

  elif choice == '1':
    while True:
      print()
      print('[학생성적입력] \n학생 성적을 입력합니다.')
      print('-'*60)
      name = input('[뒤로가기 0 입력] 학생 이름 : ')
      if name == '0':
        print('학생성적입력을 종료합니다.')
        print()
        break
      kor = int(input('국어 성적 : '))
      eng = int(input('영어 성적 : '))
      math = int(input('수학 성적 : '))
      total = kor + eng + math
      avg = total/3
      no += 1
      stulist.append([no, name, kor, eng, math, total, avg, rank])
      print('학생성적이 출력되었습니다.')

  
  elif choice == '2':
    print()
    print('                      [학생성적출력]')
    print('순번\t이름\t국어\t영어\t수학\t합계\t평균\t등수\t')
    print('-'*60)
    for i in stulist:
      print(f'{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}\t{i[6]}\t{i[7]}\t')
    print()

  elif choice == '3':
    while True:
      print()
      print('[학생성적수정] \n학생성적을 수정합니다.')
      print('-'*60)
      print('[수정항목선택]')
      print('1. 국어 성적')
      print('2. 영어 성적')
      print('3. 수학 성적')
      print('-'*60)
      re = input('[뒤로가기 0 입력] 수정할 학생의 이름을 입력하세요. >> ')
      if re == '0':
        print('학생성적수정을 종료합니다.')
        print()
        break
      for i in stulist:
        if re == i[1]:
          print(f'{i[1]} 학생을 찾았습니다. ')
          re2 = input('원하는 수정항목을 선택하세요. >>')
          if re2 == '1':
            print(f'현재 국어 점수 : {i[2]}')
            i[2] = input('수정 성적 입력 : ')
          elif re2 == '2':
            re2 == i[3]
          elif re2 == '3':
            re2 == i[4]
        else:
          print(f'{re} 학생을 찾지 못했습니다. 다시 입력하세요.')







