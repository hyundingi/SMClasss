import datetime
import os
# member 리스트 딕셔너리 저장
member = []
section_info = []
m_title = ['id','pw','name','nicname','address','money']

# 멤버 파일 불러오기 -----------------------------------
f = open('b1017/member.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line:
    break
  m = line.strip().split(',')
  m[5] = int(m[5])    # money
  # member 리스트에 딕셔너리 저장
  member.append(dict(zip(m_title,m)))
f.close()

# 상품 파일 저장해서 불러오기 -----------------------------
product = [
  {"pno":1,"pCode":"t001","pName":"삼성TV","price":2000000,"color":"black"},
  {"pno":2,"pCode":"g001","pName":"LG냉장고","price":3000000,"color":"white"},
  {"pno":3,"pCode":"h001","pName":"하만카돈스피커","price":500000,"color":"gray"},
  {"pno":4,"pCode":"w001","pName":"세탁기","price":1000000,"color":"yellow"},
]

# cart 파일 읽어오기 ---------------------------------------
cartNo = 0
cart = []
c_keys = ["cno","id","name","pCode","pName","price","date"]

if os.path.isfile('b1016/cart.txt'):
  pass
else:
  print('파일이 존재하지 않습니다.')

f = open('b1016/cart.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line:
    break
  c = line.strip().split(',')
  c[0] = int(c[0])
  c[5] = int(c[5])
  cart.append(dict(zip(c_keys,c)))
f.close()
  
# ----------- 상품 구매 함수 ----------------
def buyy():
    print(f'{product[choice-1]['pName']}를 구매하였습니다.')
    print(f'현재 잔액 : {section_info['money']-product[choice-1]['price']}')
    print((product[choice-1].values))
    print(type((product[choice-1].values)))
    #cartin = {dict(zip(list(product[choice-1].values),c_keys))}
    # cartin['cno'] = len(cart) + 1
    # cart.append(cartin)

# ---------- 프로그램 시작 ----------------------------------
while True:
  print(' [ 메인화면 ]')
  print('1. 로그인')
  print('2. 회원가입')
  print('0. 종료')
  print('-'*30)
  choice = input('원하는 번호를 입력하세요. >> ')
  
  if choice == '1':
    input_id = input('아이디를 입력하세요. >> ')
    input_pw = input('패스워드를 입력하세요. >> ')
    flag = 0
    for i in member:
      if input_id == i['id'] and input_pw == i['pw']:
        print(f'{i['nicname']}님 로그인 되었습니다.')
        section_info = i
        flag = 1
    if flag == 0:
      print('아이디 혹은 비밀번호를 다시 확인해주세요.')

  elif choice == '2':
    id = input('아이디를 입력하세요. >> ')
    flag = 0
    for i in member:
      if i['id'] == id:
        print('사용중인 아이디 입니다. 다시 입력하세요.')
        flag = 1
        break
    if flag == 0:
      print('사용 가능한 아이디 입니다.')
    pw = input('비밀번호를 입력하세요. >> ')
    name = input('이름을 입력하세요. >> ')
    nicname = input('닉네임을 입력하세요. >> ')
    address = input('주소를 입력하세요. >> ')
    money = int(input('충전할 금액을 입력하세요. >> '))
    join = [id, pw, name, nicname, address, money]
    member.append(dict(zip(m_title,join)))
    print('회원가입이 완료되었습니다.')
    

  elif choice == '0':
    print('프로그램을 종료합니다.')
    break

# 프로그램 구현 ------------------------------------------
while True:
  print()
  print('[SM-SHOP 프로그램]')
  print(f'>> {section_info['nicname']}님')
  print(f'잔액 : {section_info['money']:,d}')
  print('1. 삼성TV - 5,000,000')
  print('2. LG냉장고 - 3,000,000')
  print('3. 하만카돈스피커 - 500,000')
  print('4. 세탁기 - 1,000,000')
  print('7. 내용저장')
  print('8. 구매 내역')
  print('9. 금액충전')
  print('0. 프로그램 종료')
  choice = int(input('구매하려는 상품 번호를 입력하세요. >> '))

  if choice == 0:
    print('프로그램을 종료합니다.')
    break
  elif choice == 1:
    buyy()
  elif choice == 2:
    buyy()
  elif choice == 3:
    buyy()
  elif choice == 4:
    buyy()
  elif choice == 8:
    print(cart)

