import datetime
member = [
  {"id":"aaa", "pw":"1111", "name": "이다영", "nicname":"nana", "address":"서울특별시", "money": 1000000000},
  {"id":"bbb", "pw":"2222", "name": "권순영", "nicname":"hoshi", "address":"대구광역시", "money": 1000000000},
  {"id":"ccc", "pw":"3333", "name": "이석민", "nicname":"dk", "address":"부산시", "money": 1000000000},
  {"id":"ddd", "pw":"4444", "name": "최한솔", "nicname":"vernon", "address":"뉴욕", "money": 1000000000},
  {"id":"admin", "pw":"5555", "name": "윤정한", "nicname":"zzong", "address":"인천시", "money": 1000000000},
]
m_key = ['id','pw','name','nicname','address','money','date']
# member.txt 파일 읽기
# member에 저장
f = open('b1016/member.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line:
    break
  m = line.strip().split(',')
  m[5] = int(m[5])  # 금액
  member.append(dict(zip(m_key,m)))
f.close()

# cart.txt 파일 읽기, member 딕셔너리 저장
# print(f"{c['cno']}\t{c['id']}\t{c['name']}\t{c['pCode']}\t{c['pName']:14s}\t{c['price']}\t{c['date']}")
cartNo = 0
cart = []
c_keys = ["cno","id","name","pCode","pName","price","date"]


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
  
# ----------------------
product = [
  {'pno':1, 'pCode':'t001', 'pName':'삼성TV', 'price':2000000, 'color':'black'},
  {'pno':2, 'pCode':'g001', 'pName':'LG냉장고', 'price':3000000, 'color':'white'},
  {'pno':3, 'pCode':'h001', 'pName':'하만카돈스피커', 'price':50000000, 'color':'gray'},
  {'pno':4, 'pCode':'w001', 'pName':'세탁기', 'price':1000000, 'color':'yellow'}
]
cartNo = 0
cart = [
]
section_info = {}
p_title = ['번호', '아이디','이름','상품코드','상품명','가격','구매일자']

# ----------- 장바구니 함수선언 -----------
def buy(cartNo,choice):
  print(f'{product[choice-1]['pName']} 를 구매하셨습니다.')
  print('구매내역에 저장됩니다.')
  print()
  # 로그인 정보 - section_info
  now = datetime.datetime.now()
  today = now.strftime('%Y-%m-%d %H:%M:%S')
  c = {'cno':cartNo+1, 'id':section_info['id'], 'name':section_info['name'],'pCode':product[choice-1]['pCode'], 'pName':product[choice-1]['pName'],'price':product[choice-1]['price'], 'date':today}
  section_info['money'] -= product[choice-1]['price']
  cart.append(c)
  cartNo += 1
  return cartNo

# ----------- 구매 내역 출력 ----------------
def buy_output():
  print(f'{p_title[0]}\t{p_title[1]}\t{p_title[2]}\t{p_title[3]}\t{p_title[4]}\t{p_title[5]}\t{p_title[6]}\t')
  sum = 0
  for tc in cart:
    sum += tc['price']
    print(f'{tc['cno']}\t{tc['id']}\t{tc['name']}\t{tc['pCode']}\t{tc['pName']:10}\t{tc['price']}\t{tc['date']}\t')
  print('총 구매 건수 : ', len(cart))
  print('총 구매 금액 : ', sum)

# ----------- 금액 충전 ----------------------
def buy_money():
  print(f'현재 금액 : {section_info['money']}')
  plus = int(input('충전할 금액 입력 >> '))
  section_info['money'] += plus
  print(f'충전이 완료되었습니다. 현재 금액 : {section_info['money']}')

# --------------
def buy_save():
  f = open('b1016/member.txt','w',encoding='utf-8')
  for i in member:
    f.write(f'{i['id']},{i['pw']},{i['name']},{i['nicname']},{i['address']},{i['money']}\n')
  f.close()
# cart.txt 파일생성해서 csv형태로 문자열로 저장하시오.
  f = open('b1016/cart.txt','w',encoding='utf-8')
  for c in cart:
    f.write(f"{c['cno']},{c['id']},{c['name']},{c['pCode']},{c['pName']},{c['price']},{c['date']}\n")
  f.close()
  print("내용저장이 완료되었습니다.")
  print()


# ---------- 프로그램 시작 ---------------
while True:
  print(' [ LOGIN ]')
  input_id = input('아이디를 입력하세요. >> ')
  input_pw = input('패스워드를 입력하세요. >> ')

  # db에서 가져옴
  # member 데이터를 가지고 비교
  flag = 0
  for m in member:
    if m['id'] == input_id and m['pw'] == input_pw:
      print(f'{m['nicname']}님! SM SHOP에 오신 것을 환영합니다.')
      section_info = m
      flag = 1
      break   # for반복문
  if flag == 0:
    print('아이디 또는 패스워드가 일치하지 않습니다.')
  else: 
    break
  

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
  choice = int(input('구매하려는 상품 번호를 입력하세요. >> '))

  if choice == 1:
    cartNo = buy(cartNo,choice)   # 상품구매함수 호출
    print(cart)
  elif choice == 2:
    cartNo = buy(cartNo,choice)   # 상품구매함수 호출
  elif choice == 3:
    cartNo = buy(cartNo,choice)   # 상품구매함수 호출
  elif choice == 4:
    cartNo = buy(cartNo,choice)   # 상품구매함수 호출
  elif choice == 7:
    buy_save()        # 내용저장함수 호출

  elif choice == 8:
    buy_output()
  elif choice == 9:
    buy_money()
    

  
