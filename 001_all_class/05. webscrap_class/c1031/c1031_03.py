# 오라클 db에서는 타입이 결정되어 문자형(숫자만) 타입 + 숫자와 사칙연산 가능
# 파이썬에서 호출한 타입의 결과값이 어떻게 되는 지 확인

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

conn = connects()
cursor = conn.cursor()
## chartable : number, number, varchar2, varchar2
## chartable2 : number, number, number, number
# sql = 'select * from chartable'
sql = "select no, kor, to_char(ko_char, '00000000'), to_char(kor_mark, '999,999,999') from chartable"
cursor.execute(sql)
rows = cursor.fetchall()

for row in rows:
  # print(f'두 수의 합 : {row[1]+row[0]}')
  # print(f'두 수의 합 : {row[1]+row[2]}')    # 오라클에서는 가능/ 파이썬에서는 안 됨
  print(row)

print('검색완료')
conn.close()

