# 학생성적프로그램
# 1. 학생성적입력
# 2. 학생성적출력
# 3. 학생성적검색
# students 테이블 사용 / 번호 김유신 99 98 96 합계 평균 등수 / students_seq 생성 후 번호 삽입

import oracledb

def connects():
  user = 'ora_user'
  password = '1111'
  dsn = 'localhost:1521/xe'
  try:
    conn = oracledb.connect(user=user, password=password, dsn=dsn)
  except Exception as e:
    print('에러 발생 : ', e)
  return conn

while True:
  print('[학생성적프로그램]')
  print('1. 학생성적입력')
  print('2. 학생성적출력')
  print('3. 학생성적검색')
  choice = input('원하는 번호 입력 >> ')

  if choice == '1':
    name = input('이름을 입력하세요. >> ')
    kor = int(input('국어점수를 입력하세요. >> '))
    eng = int(input('영어점수를 입력하세요. >> '))
    math = int(input('수학점수를 입력하세요. >> '))
    total = kor+eng+math
    avg = round(total/3, 2)
    rank = 0
  # db접속
    # 데이터 입력받아 mem 테이블에 넣기
    conn = connects()
    cursor = conn.cursor()
    sql = 'insert into students values(students_seq.nextval, :name, :kor, :eng, :math, :total, :avg, :rank, sysdate)'
    cursor.execute(sql, name=name, kor=kor, eng=eng, math=math, total=total, avg=avg, rank=rank)
    conn.commit()
    conn.close()


  elif choice == '2':
    conn = connects()
    cursor = conn.cursor()
    sql = 'select * from students'
    cursor.execute(sql)
    rows = cursor.fetchall()

    print('[학생성적출력]')
    print('NO\t이름\t국어\t영어\t수학\t합계\t평균\t등수\t등록일\t')
    print('-'*80)
    for row in rows:
      for i in row:
        if type(i) == float:
          print(round(i,2), end='\t')
        else:
          print(i, end = '\t')
      print()
    
    conn.close()



  elif choice == '3':
    name = input('검색할 학생의 이름을 입력하세요. >> ')
    conn = connects()
    cursor = conn.cursor()
    sql = 'select * from students where name=:name'
    cursor.execute(sql, name=name)
    row = cursor.fetchone()

    if row == None:
      print('없는 학생입니다. 다시 입력하세요. ')
      continue
    
    print(f'[{name} 학생의 성적]')
    print('NO\t이름\t국어\t영어\t수학\t합계\t평균\t등수\t등록일\t')
    print('-'*80)
    for i in row:
      print(i, end='\t')
      

    conn.close()
