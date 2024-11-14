# employees 테이블에서 이름이 a가 포함되어 있는 모든컬럼 출력

import oracledb

# db  연결 함수 ㅔ
def connections():
  try:
    conn = oracledb.connect(user='ora_user', password='1111', dsn='localhost:1521/xe')
    print('db연결 : ', conn.version)
  except Exception as e:
    print*('예외 발생', e)
  return conn

# 함수 호출
conn = connections()
cursor = conn.cursor()

# 월급이 4000~8000 사이의 사원 출력
money = input('급여 입력 (쉼표 구분) >> ')
m_list = money.split(',')
sql = 'select employee_id, emp_name, salary from employees where salary between :1 and :2 order by salary'
cursor.execute(sql, m_list)

# sql = "select * from employees where emp_name like '%a%'"
# cursor.execute(sql)

# 입력한 값이 이름에 포함되어 있는 데이터 검색 
# search = input('검색할 이름을 입력하세요. >> ') 
# search = '%' + search + '%'
# sql = 'select * from employees where emp_name like :search'
# cursor.execute(sql,search=search)

# 번호 입력해서 그 번호보다 이후 데이터 출력
# search = input('번호 검색 >> ')
# sql = "select * from employees where employee_id >= :search"
# cursor.execute(sql, search=search)

# 번호 입력해서 그 번호보다 이후 데이터 출력
# search = input('번호 검색 >> ')
# sql = 'select * from employees where employee_id >= :1'
# cursor.execute(sql,[search,])

title = ['employee_id', 'emp_name', 'salary']
a_list = [] # dict 타입으로 변경해서 저장
rows = cursor.fetchall()
for row in rows:
  a_list.append(dict(zip(title,row)))
print(a_list)