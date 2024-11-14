import oracledb
import datetime

nowYear = datetime.datetime.now().year


def connects():
  user = 'ora_user'
  password = '1111'
  dsn = 'localhost:1521/xe'
  try:
    conn = oracledb.connect(user=user, password=password, dsn=dsn)
  except Exception as e:
    print('에러 발생 : ', e)
  return conn

def member_count():
  # 오라클 디비 ㅡmem 테이블의 count 를 가져오시오
  conn = connects()
  cursor = conn.cursor()
  sql = 'select count(*) from member'
  # employees 테이블 부서번호 10번인 사원 수
  sql = 'select count(*) from employees where DEPARTMENT_ID = 50'
  # employees 테이블 부서번호 부서명
  sql = 'select count(*), a.department_id, department_name from employees a, departments b where a.department_id = b.department_id and a.department_id = 50 group by a.department_id, department_name'
  cursor.execute(sql)
  row = cursor.fetchone()

  return row


## 회원수 확인값을 리턴
all_member = member_count()

print(' [커뮤니티] ')
print(f'현재 회원 수 : {all_member[0]}, 부서번호 : {all_member[1]}, 부서명 : {all_member[2]}')
print()
print('1. 로그인')
print('2. 회원가입')
print('3. 회원정보수정')
choice = input('원하는 번호를 입력하세요. >> ')

if choice == '2':
  id = input('아이디를 입력하세요 >> ')
  pw = input('비밀번호를 입력하세요. >> ')
  name = input('이름을 입력하세요. >> ')
  birth = input('생년월일을 입력하세요. (ex. 20020312) >> ')
  age = nowYear-int(birth[:4])  # 나이 자동 계산
  genders = input('성별을 입력하세요. \n 1) Female  2) Male >> ')
  if genders == '1':
    gender = 'Female'
  elif genders == '2':
    gender = 'Male'
  hobby = input('취미를 입력하세요. >> ')

  my_list = [id,pw,name,age,birth,gender,hobby]
  print(my_list)

  # db접속
  # 데이터 입력받아 mem 테이블에 넣기
  conn = connects()
  cursor = conn.cursor()
  sql = 'insert into mem (id, pw, name, age, birth, gender, hobby) values (:1, :2, :3, :4, :5, :6, :7)'
  sql = 'insert into mem (id, pw, name, age, birth, gender, hobby) values (:id, :pw, :name, :age, :birth, :gender, :hobby)'
  cursor.execute(sql, id=id, pw=pw, name=name, age=age, birth=birth, gender=gender, hobby=hobby)
  conn.commit()
  conn.close()

elif choice == '3':
  id = input('아이디를 입력하세요 >> ')

  id = 'aaa'
  conn = connects()
  cursor = conn.cursor()
  sql = 'select * from mem where id=:id'
  cursor.execute(sql, id=id)
  row = cursor.fetchone()
  print(f'아이디 : {row[0]} , 현재 취미 : {row[6]}')
  
  hobby = input('수정할 취미를 입력하세요. >> ')
  sql = 'update mem set hobby=:hobby where id=:id'
  cursor.execute(sql, hobby=hobby, id=id)
  conn.commit()
  conn.close()