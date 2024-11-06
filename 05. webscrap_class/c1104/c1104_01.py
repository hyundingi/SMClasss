import oracledb

s_title = ['번호','이름','국어','영어','수학','합계','평균','등수','등록일']

# db연결 함수선언
def connects():
  user = 'ora_user'
  password = '1111'
  dsn = 'localhost:1521/xe'
  try:
    conn = oracledb.connect(user=user, password=password, dsn=dsn)
  except Exception as e:
    print('예외처리')

  return conn


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
    conn = connects()
    cursor = conn.cursor()
    print('[학생성적입력]')
    sql = 'select students_seq.nextval from dual'
    cursor.execute(sql)
    row = cursor.fetchone()

    no = row[0]
    name = input(f'{no}번 학생이름을 입력하세요. >> ')
    kor = int(input('국어점수 입력 >> '))
    eng = int(input('영어점수 입력 >> '))
    math = int(input('수학점수 입력 >> '))
    total = kor+eng+math
    avg = round(total/3,2)
    # list
    s_list = [name, kor, eng, math, total, avg]

    # insert, update, delete 경우 conn.commit() 해야 반영됨
    sql = 'insert into students values(students_seq.nextval, :1, :2, :3, :4, :5, :6, 0, sysdate)'
    cursor.execute(sql, s_list)
    conn.commit()
    conn.close()

    

  elif choice == '2':
    print('[학생성적출력]')
    for s in s_title:
      print(s, end='\t')
    print()
    print('-'*80)

    conn = connects()
    cursor = conn.cursor()
    sql = "select no, name, kor, eng, math, total, round(avg,2), rank, to_char(sdate, 'yyyy-mm-dd') from students"
    cursor.execute(sql)
    rows = cursor.fetchall()
    
    if len(rows) < 1:
      print('데이터가 없습니다.')
      break
    for row in rows:
      for r in row:
        print(r, end='\t')
      print()
    print()
    print('데이터 출력 완료 ------')

    cursor.close()

  elif choice == '3':
    conn = connects()
    cursor = conn.cursor()

    print('[학생성적검색]')
    print('1. 이름으로 검색')
    print('2. 합계순 검색')
    choice = input('원하는 번호를 입력하세요. >> ')

    if choice == '1':
      print('[이름으로검색]')
      search = input('찾고자하는 이름 검색 >> ')
      search = '%'+search+'%'
      sql = "select * from students where name like :search"
      cursor.execute(sql,search=search)
      rows = cursor.fetchall()
      for s in s_title:
        print(s, end='\t')
      print()
      print('-'*80)
      for row in rows:
        for r in row:
          print(r, end='\t')
        print()
      print()
      print('데이터 출력 완료 ------')

    elif choice == '2':
      sql = "select * from students order by avg where"
      cursor.execute(sql,search=search)
      rows = cursor.fetchall()
      for s in s_title:
        print(s, end='\t')
      print()
      print('-'*80)
      for row in rows:
        for r in row:
          print(r, end='\t')
        print()
      print()
      print('데이터 출력 완료 ------')
      
    conn.close()

  elif choice == '4':
    conn = connects()
    cursor = conn.cursor()

    print('[정렬]')
    print('1. 이름순차정렬')
    print('2. 이름역순정렬')
    choice = input('원하는 번호를 입력하세요. >> ')

    if choice == '1':
      sql = "select no, name, kor, eng, math, total, round(avg,2), rank, to_char(sdate,'yyyy-mm-dd') from students order by name"
      cursor.execute(sql)
      rows = cursor.fetchall()
      for s in s_title:
        print(s, end='\t')
      print()
      print('-'*80)
      for row in rows:
        for r in row:
          print(r, end='\t')
        print()
      print()
      print('데이터 출력 완료 ------')

    elif choice == '2':
      sql = "select no, name, kor, eng, math, total, round(avg,2), rank, to_char(sdate,'yyyy-mm-dd') from students order by name desc"
      cursor.execute(sql)
      rows = cursor.fetchall()
      for s in s_title:
        print(s, end='\t')
      print()
      print('-'*80)
      for row in rows:
        for r in row:
          print(r, end='\t')
        print()
      print()
      print('데이터 출력 완료 ------')
    conn.close()

  elif choice == '5':
    conn = connects()
    cursor = conn.cursor()
    sql = 'update students a set rank = (select ranks from (select no, rank() over(order by avg desc) ranks from students) b where a.no = b.no)'
    cursor.execute(sql)
    conn.commit()
    print('[등수처리완료]')

    sql = "select no, name, kor, eng, math, total, round(avg,2), rank, to_char(sdate,'yyyy-mm-dd') from students"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for s in s_title:
      print(s, end='\t')
    print()
    print('-'*80)
    for row in rows:
      for r in row:
        print(r, end='\t')
      print()
    print()
    print('데이터 출력 완료 ------')
    conn.close()


  elif choice == '0':
    print('프로그램을 종료합니다.')
    break

# 학생성적프로그램
# 1. 학생성적입력
# 2. 학생성적출력
# 3. 학생성적검색
# students 테이블 사용 / 번호 김유신 99 98 96 합계 평균 등수 / students_seq 생성 후 번호 삽입

