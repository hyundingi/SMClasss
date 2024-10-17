# member 리스트 딕셔너리 저장
member = []
m_title = ['id','pw','name','nicname','address','money']


# 파일 불러오기
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

# 아이디 검색
# 입력한 데이터가 들어가 있는 아이디 모두 출력
while True:
  print('1. 회원가입')
  print('2. 회원검색')
  choice = input('원하는 번호를 입력하세요. >> ')
  if choice == '1':
    id = input('ID를 입력하세요. >> ')
    flag = 0
    for m in member:
      if m['id'] == id:
        print('동일한 ID가 있습니다. 다시 입력하세요.')
        flag = 1
        break
    if flag == 1:
      continue
    else:
      print('사용가능한 ID 입니다.')
    pw = input('PW를 입력하세요. >> ')
    name = input('이름을 입력하세요 >> ')
    nicname = input('닉네임을 입력하세요 >> ')
    address = input('주소를 입력하세요. >> ')
    money = int(input('충전할 금액을 입력하세요. >> '))
    m_list = [id,pw,name,nicname,money]
    member.append(dict(zip(m_title,m_list)))
    print(f'{id} 님 회원가입 완료')
    print(m_list)

  elif choice == '2':
    search = input('검색창 : ')
    flag = 0
    mm = []
    for i in member:
      if i['name'].find(search)>-1:
        print(i)
        mm.append(i)
        flag = 1
    if flag == 0:
      print('없는 회원입니다.')
    else:
      print('총 검색된 인원 : ', len(mm))