import oracledb

# sql developer 실행
conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')

# sql 창이 열림
cursor = conn.cursor()

# sql 작성, 실행
# no = 10,20,30 을 검색해서 출력
num = input('숫자를 입력하세요. >> ')
# 10, 20, 30
n_list = num.split(',')
# excute 함수 : 리스트 값 전달

# 1. 문자열 함수 f열 사용
# sql = f'select * from students where no >= {num}'
# 2. excute 함수 : 변수의 key값 전달
# sql = 'select * from students where no >= :no'
# 3. excute 함수 : 리스트 값 전달
# execute 뒤에는 dict, list, tuple 타입만 가능
sql = 'select * from students where no in (:1, :2, :3)'
cursor.execute(sql, n_list)

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
