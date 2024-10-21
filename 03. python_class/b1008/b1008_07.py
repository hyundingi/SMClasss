import operator

students = [
  {'no':1,'name': "홍길동",'kor':100,'eng':100,'math':99,'total':299,'avg':99.67,'rank':0},
  {'no':2,'name': "유관순",'kor':80,'eng':80,'math':85,'total':245,'avg':81.67,'rank':0},
  {'no':3,'name': "이순신",'kor':90,'eng':90,'math':91,'total':271,'avg':90.33,'rank':0},
  {'no':4,'name': "강감찬",'kor':60,'eng':65,'math':67,'total':192,'avg':64.00,'rank':0},
  {'no':5,'name': "김구",'kor':100,'eng':100,'math':84,'total':284,'avg':94.67,'rank':0},
]

# zip() 함수
# 동시에 여러개 리스트에 접근
# name = ['홍길동','유관순','이순신']
# score = [100,90,95]

## 딕셔너리 타입의 리스트 생성
# d_dic = dict(zip(name,score))
# print(d_dic)  # 출력값 : {'홍길동': 100, '유관순': 90, '이순신': 95}

## 튜플타입 리스트 생성 (수정 불가)
# n_list = list(zip(name,score))
# print(n_list)  # 출력값 : [('홍길동', 100), ('유관순', 90), ('이순신', 95)]

## 리스트 타입
# n_list = []
# for n,s in zip(name, score):
#   n_list.append([n,s])
# print(n_list)  # 출력값 : [['홍길동', 100], ['유관순', 90], ['이순신', 95]]


# 리스트에 값 추가 방법
# for를 사용해서 1,2,3,4,5 넣기
# numList = []
# for i in range(5):
#   numList.append(i+1)
# print(numList)

# # for문을 1줄로 사용해서 처리
# # 리스트 내포, 컴프리헨션
# nList = [i+1 for i in range(5)]
# print(nList)

# a_list = [i*i for i in range(5)]
# print(a_list)

# # 정수형 > 문자열로 바꾸어 넣는 리스트 내포(1줄 for문)
# b_list = [str(i) for i in range(5)]
# print(b_list)

# # 문자열 > 정수형으로 바꾸어 넣는 리스트 내포
# c_list = ['5','9','0','3','2']
# cc_list = [int(i) for i in c_list ]
# print(cc_list)

# d_str = '1,2,23,5,9'
# d_sp = [int(i) for i in d_str.split(',')]
# print(d_sp)


# # 문자열을 입력받아 숫자형 리스트로 변경
# score = input('좌표를 입력하세요. >> ')
# sc = [int(i) for i in score.split(',')]
# print(score)
# print(sc)




# print(students)
# x = sorted(students.items())
# print('-'*50)
# print(students)





# nameDic = {'홍길동': 100, '유관순':80, '이순신':95, '강감찬':82, '김구':97}

#key 값만 가져오는 방법 :: nameDic.key()
#value 값만 가져오는 방법 :: nameDic.value()
#key, value 값을 모두 가져오는 방법 :: nameDic.items()
# print(nameDic)
# key - [0], value - [1]
# (key, value) : [0,1]
# nameDics = sorted(nameDic.items())               # 0번째 기준으로 순차 정렬
# nameDics = sorted(nameDic.items(), reverse=True) # 0번째 기준으로 역순 정렬
# nameDics = sorted(nameDic.items(), key=operator.itemgetter(1))  # 1번째 기준으로 순차정렬
# nameDics = sorted(nameDic.items(), key=operator.itemgetter(1), reverse=True)  # 1번째 기준으로 역순정렬


# lambda x:x[0], lambda x:x[1]
# print('-'*50)
# print(nameDics)