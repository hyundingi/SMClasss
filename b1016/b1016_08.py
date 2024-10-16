# member 파일 읽어와서 member 딕셔너리 저장
# cart 파일 읽고, cart 저장

# 프로그램 시작 화면 구현/상품구매
member = []
m_key = ['id','pw','name','nicname','address','money']

# ---- 회원 목록 (member) 불러오기 -----
f = open('b1016/member.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line:
    break
  k = line.strip().split(',')
  k[5] = int(k[5])
  member.append(dict(zip(m_key,k)))

# -------- 로그인 --------
shop_id = input('아이디를 입력하세요. >> ')
shop_pw = input('비밀번호를 입력하세요. >> ')

flag = 0
for i in member:
  if i['id'] == shop_id and i['pw'] == shop_pw:
    print(f'{i['nicname']}님 어세오세요!')
    flag = 1
  if flag == 0:
    print('아이디 또는 비밀번호가 맞지 않습니다. 다시 입력하세요.')

while True:
  print('[가게]')
  print('1. 상의 : 50,000')
  print('2. 하의 : 40,000')
  print('3. 신발 : 100,000')
  print('4. 가방 : 200,000')
  choice = input('구매하실 상품의 번호를 입력하세요. >> ')

  if choice == '0':
    break
  elif choice == '1':
    print('상의를 구매하셨습니다.')