member = [
  {'id':'aaa', 'pw':'111','name':'홍길동', 'nicname':'길동스','address':'서울', 'money':100000000},
  {'id':'bbb', 'pw':'222','name':'유관순', 'nicname':'관순스','address':'부산', 'money':70000000},
  {'id':'ccc', 'pw':'333','name':'이순신', 'nicname':'순신스','address':'경기', 'money':20000000},
  {'id':'ddd', 'pw':'444','name':'강감찬', 'nicname':'감찬스','address':'인천', 'money':50000000},
  {'id':'eee', 'pw':'555','name':'김구', 'nicname':'김스','address':'대구','money':50000000}
]

# member.txt 파일 생성 csv 형식으로 내용 저장

f = open('b1016/member.txt','w',encoding='utf-8')

for i in member:
  f.write(f'{i['id']},{i['pw']},{i['name']},{i['nicname']},{i['address']},{i['money']},{i['date']}\n')
f.close()


# # 딕셔너리로 묶는법~
# # a = ['no', 'name', 'kor', 'eng']
# # b = [1,'홍길동',100,100]
# # print(dict(zip(a,b)))

# # a = ['홍길동', '유관순', '이순신']
# # b = [100,92,80]
# # c = zip(a,b)
# # print(dict(c))
# # print(list(c))

# students = [
#   {'no': 1, 'name': '홍길동', 'kor': 33, 'eng': 33, 'math': 33, 'total': 99, 'avg': 33.0, 'rank': 0},
#   {'no': 2, 'name': '유관순', 'kor': 55, 'eng': 55, 'math': 55, 'total': 165, 'avg': 55.0, 'rank': 0},
#   {'no': 3, 'name': '이순신', 'kor': 11, 'eng': 11, 'math': 11, 'total': 33, 'avg': 11.0, 'rank': 0}
# ]


# # students 딕셔너리 파일을 메모장에 csv 형식으로 저장
# f = open('b1016/students.txt', 'w', encoding='utf-8')

# for i in students:
#   f.write(f'{i['no']},{i['name']},{i['kor']},{i['eng']},{i['math']},{i['total']},{i['avg']},{i['rank']}\n')
# f.close()