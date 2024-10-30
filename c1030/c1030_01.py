import oracledb
import random
# email 발송관련
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

a = random.randrange(1000,10000)
ran_num = '{}'.format(a)

# 랜덤 4자리 숫자
print(ran_num)

def connects():
  user = 'ora_user'
  password = '1111'
  dsn = 'localhost:1521/xe'
  try:
    conn = oracledb.connect(user=user, password=password, dsn=dsn)
  except Exception as e:
    print('예외발생 : ', e)
  return conn

def mailling():
  smtpName = 'smtp.naver.com'
  smtpPort = 587


  # id, pw, 받는사람이메일주소
  sendEmail = 'qo0723@naver.com'
  pw = 'N41S7SY2HVQN'
  recvEmail = 'qo0723@naver.com'

  title = '임시비밀번호 발급'
  content = '임시비밀번호 : {} 입니다.'.format(ran_num)
  msg = MIMEMultipart()
  msg['Subject'] = title
  msg['From'] = sendEmail
  msg['To'] = recvEmail
  msg.attach(MIMEText(content))

  s = smtplib.SMTP(smtpName, smtpPort)
  s.starttls()   # 보안 인증
  s.login(sendEmail,pw)
  s.sendmail(sendEmail,recvEmail,msg.as_string())
  print('msg : ')
  print(msg.as_string)
  s.quit()

  print('메일발송완료')


while True:
  print('[ 커뮤니티 ]')
  print('1. 로그인')
  print('2. 비밀번호 찾기')
  print('3. 회원가입')
  print('0. 종료')
  print('-'*30)
  choice = input('원하는 번호를 입력하세요. >> ')

  if choice == '0':
    print('프로그램을 종료합니다.')
    break

  elif choice == '1':
    user_id = input('아이디를 입력하세요. >> ')
    user_pw = input('패스워드를 입력하세요. >> ')

    # 오라클 db에 접속해서 member 테이블에서 검색하여 가져옴
    conn = connects()
    cursor = conn.cursor()
    sql = 'select * from member where id=:id and pw=:pw'
    cursor.execute(sql, id = user_id, pw = user_pw)
    row = cursor.fetchone()
    print(row)

    if len(row) != None:
      print(f'로그인 성공! {row[2]}님, 환영합니다.')
    else:
      print('아이디 또는 패스워드가 일치하지 않습니다. 정확히 입력하세요!!!')
      continue

    cursor.close()
    # if user_id == 'aaa' and user_pw == '1111':
    #   print('로그인 성공')
    # else:
    #   print('로그인 실패')
    #   continue

    print('학생성적프로그램에 접속합니다.')
    ## 프로그램 구현

  elif choice == '2':
    print('[ 비밀번호 찾기 ]')
    search = input('해당 아이디를 입력하세요. >> ')

    conn = connects()
    cursor = conn.cursor()
    sql = 'select * from member where id = :id'
    cursor.execute(sql, id=search)
    row = cursor.fetchone()

    if row != None:
      print('아이디가 존재합니다. 임시패스워드를 발급합니다. ')
      mailling()
      # 1. 임시비밀번호 생성
      # 2. 이메일로 보냄
      # 3. 아이디 비밀번호 > 임시비밀번호로 수정
      # 4. 임시번호로 로그인 햇을 경우 성공
      sql = 'update member set pw = :pw where id = :id'
      cursor. execute(sql, id=search, pw=ran_num)
      conn.commit()
    else:
      print('아이디가 존재하지 않습니다.')
    
    cursor.close()


  elif choice == '3':
    pass