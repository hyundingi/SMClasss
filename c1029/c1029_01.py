import oracledb

# sql developer 실행
conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')

# sql 창이 열림
cursor = conn.cursor()

# sql 작성, 실행
sql = 'select * from students'
cursor.execute(sql)

# 데이터 가져오기 - fetchone(): 한개 가져오기, fetchmany(10): 정해진 숫자만큼 가져오기, fetchall(): 싹 다 가져오기
rows = cursor.fetchall()
titles = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수', '등록일']

for title in titles:
  if title == '이름':
    print(f'{title:9s}', end='\t')
    continue
  print(title, end='\t')
print()
print('-'*80)

for row in rows:
  for i, r in enumerate(row):
    if i == 1:
      print(f'{r:12s}', end='\t')
      continue
    if i == 6:
      print(f'{r:.2f}', end='\t')
      continue
    if i == 8:
      # strftime()힘스 : 날짜 포맷 함수 %Y : 2024 %y 2024,%y:24
      print(r.strftime('%y-%m-%d'))
      # print(f'{r[1]}', end='\t')
      continue
    print(r, end = '\t')
  print()

# 종료
conn.close()
