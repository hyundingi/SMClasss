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

# 프린트 함수 선언
def stu_p(rows):
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

# 학생성적입력 함수선언
def stu_insert():
  conn = connects()
  cursor = conn.cursor()
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

# 학생성적출력 함수 선언
def stu_print(s_title):
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
    

  for row in rows:
    for r in row:
      print(r, end='\t')
    print()
  print()
  print('데이터 출력 완료 ------')

  cursor.close()

# 학생성적검색 함수 선언
def stu_search(choice, s_title):
  conn = connects()
  cursor = conn.cursor()

  if choice == '1':
    print('[이름으로검색]')
    search = input('찾고자하는 이름 검색 >> ')
    search = '%'+search+'%'
    sql = "select * from students where name like :search"
    cursor.execute(sql,search=search)
    rows = cursor.fetchall()
    stu_p(rows)
    

  elif choice == '2':
    sql = "select * from students order by avg where"
    cursor.execute(sql,search=search)
    rows = cursor.fetchall()
    stu_p(rows)
    
  conn.close()

# 학생성적정렬 함수 선언
def stu_line(choice, s_title):
  conn = connects()
  cursor = conn.cursor()
  if choice == '1':
    sql = "select no, name, kor, eng, math, total, round(avg,2), rank, to_char(sdate,'yyyy-mm-dd') from students order by name"
    cursor.execute(sql)
    rows = cursor.fetchall()
    stu_p(rows)
  

  elif choice == '2':
    sql = "select no, name, kor, eng, math, total, round(avg,2), rank, to_char(sdate,'yyyy-mm-dd') from students order by name desc"
    cursor.execute(sql)
    rows = cursor.fetchall()
    stu_p(rows)
  conn.close()

# 학생등수처리 함수
def stu_rating(s_title):
  conn = connects()
  cursor = conn.cursor()
  sql = "update students a set rank = (select ranks from (select no, rank() over(order by avg desc) ranks from students) b where a.no = b.no)"
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