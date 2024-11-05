import stu_func



while True:
  print('[학생성적프로그램]')
  print('1. 학생성적입력')
  print('2. 학생성적출력')
  print('3. 학생성적검색')
  print('4. 학생성적정렬')   # 이름 순차정렬, 이름 역순정렬, 합계 순차정렬, 합계 역순정렬
  print('5. 등수처리')
  print('0. 프로그램 종료')
  choice = input('원하는 번호를 입력하세요. >> ')

  if choice == '1':
    print('[학생성적입력]')

    # 학생성적입력 함수 호출
    stu_func.stu_insert()

  elif choice == '2':
    print('[학생성적출력]')

    # 학생성적출력 함수 호출
    stu_func.stu_print()
    
  elif choice == '3':
    print('[학생성적검색]')
    print('1. 이름으로 검색')
    print('2. 합계순 검색')
    choice = input('원하는 번호를 입력하세요. >> ')

    # 학생성적검색 함수 호출
    stu_func.stu_search(choice)
    
  elif choice == '4':
    print('[정렬]')
    print('1. 이름순차정렬')
    print('2. 이름역순정렬')
    choice = input('원하는 번호를 입력하세요. >> ')

    # 학생성적정렬 함수 호출
    stu_func.stu_line(choice)

  elif choice == '5':
    # 등수처리 호출 함수
    stu_func.stu_rating()


  elif choice == '0':
    print('프로그램을 종료합니다.')
    break

# 학생성적프로그램
# 1. 학생성적입력
# 2. 학생성적출력
# 3. 학생성적검색
# students 테이블 사용 / 번호 김유신 99 98 96 합계 평균 등수 / students_seq 생성 후 번호 삽입

