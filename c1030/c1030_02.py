import oracledb
import random
a_list = [0,1,2,3,4,5,6,7,8,9]

a = random.randrange(0,10000)
ran_num = '{:4}'.format(a)

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
    sql = 'update member set pw = :pw where id=:id'
    cursor.execute(sql, id = user_id, pw = user_pw)
    conn.commit()
    print('파일이 수정되었습니다.')


    if len(row) >= 1:
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
      # 
    else:
      print('아이디가 존재하지 않습니다.')
    
    cursor.close()