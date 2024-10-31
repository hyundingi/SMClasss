## 입력한 달 이상 입사한 사원
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

d_day = int(input('숫자를 입력하세요. >> '))

sql = 'select * from employees where to_number(substr(hire_date,4,2)) >= :d_day order by hire_date'
cursor.execute(sql, d_day=d_day)
rows = cursor.fetchall()

for row in rows:
  print(row[1], row[4])

conn.close()