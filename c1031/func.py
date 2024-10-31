import random
import oracledb
import smtplib
from email.mime.text import MIMEText

# 시작화면 함수선언
def screen():
  print('[ 커뮤니티 ]')
  print('1. 로그인')
  print('2. 비밀번호 찾기')
  print('3. 회원가입')
  print('4. 프로그램 종료')
  choice = input('원하는 번호를 입력하세요. >> ')
  return choice

# 1번 로그인 함수 선언
def memLogin():
  user_id = input('아이디를 입력하세요. >> ')
  user_pw = input('패스워드를 입력하세요. >> ')

  # db접속
  conn = connect()
  cursor = conn.cursor()
  sql = 'select * from member where id = :id and pw = :pw'
  cursor.execute(sql, id=user_id, pw=user_pw)
  row = cursor.fetchone()
  cursor.close() # db 연결 해제

  if row == None:
    print('아이디 또는 패스워드가 일치하지 않습니다. 다시 입력하세요. ')
    return
  else:
    # 이후 프로그램 구성 예정
    print(f'{row[2]}님 환영합니다.')
    print('[학생성적프로그램]')
    print('1. 학생성적 입력')
    print('2. 학생성적 출력')
    print('')

# db 연결 함수 선언
def connect():
  user = 'ora_user'
  password = '1111'
  dsn = 'localhost:1521/xe'
  try:
    conn = oracledb.connect(user=user, password=password, dsn=dsn)
  except Exception as e:
    print('예외처리 : ', e)
  return conn

# 2번 비밀번호 찾기 함수 선언
def search_pw():
  user_id = input('아이디를 입력하세요. >> ')
    
  # db접속
  conn = connect()
  cursor = conn.cursor()
  sql = 'select * from member where id = :id'
  cursor.execute(sql, id=user_id)
  row = cursor.fetchone()
  
  if row == None:
    print('아이디가 존재하지 않습니다. 다시 입력하세요!')
    return
  
  else:
    input(f'[{row[0]}] 아이디가 존재합니다. 임시 비밀번호를 발급 enter ')
    # 이메일 발송 함수 호출
    random_pw = emailSend(row[3])

    # 임시비밀번호를 update
    sql = 'update member set pw = :pw where id = :id'
    cursor.execute(sql, pw = random_pw, id = user_id)
    conn.commit()
  cursor.close() # db 연결 해제

# 임시 비밀번호 생성 (랜덤숫자 4자리)
def random_pw():
  a = random.randrange(0,10000)
  ran_num = f'{a:04}'
  print('랜덤번호 : ', ran_num)
  return ran_num

# email 발송 함수선언
def emailSend(email):
  smtpName = 'smtp.naver.com'
  smtpPort = 587

  sendEmail = 'qo0723@naver.com'
  pw = 'N41S7SY2HVQN'
  recvEmail = email

  title = '[메일발송] 임시 비밀번호 발급'
  ran_num = random_pw()
  content = f'임시 비밀번호 : {ran_num}'

  # 설정
  msg = MIMEText(content)
  msg['subject'] = title
  msg['From'] = sendEmail
  msg['To'] = recvEmail

  # 서버이름, 서버포트
  s = smtplib.SMTP(smtpName,smtpPort)
  s.starttls()
  s.login(sendEmail, pw)
  s.sendmail(sendEmail,recvEmail,msg.as_string())
  s.quit()

  # 메일발송완료
  print('메일 발송 완료')

  return ran_num