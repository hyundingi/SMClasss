subject = ['국어','영어','수학','과학','역사']
score = []
sum = 0


while True:
  print('1. 과목 추가')
  print('0. 종료')

  choice = input('원하는 번호를 입력하세요. >> ')
  if choice == '1':
    s_input = input('과목을 추가하세요. >> ')
    subject.append(s_input)
  elif choice == '0':
    break

for i in range(len(subject)):
  score.append(int(input(f'{subject[i]} 점수를 입력하세요. >> ')))

# num1 = int(input('국어 점수를 입력하세요. >> '))
# num2 = int(input('영어 점수를 입력하세요. >> '))
# num3 = int(input('수학 점수를 입력하세요. >> '))
# num4 = int(input('과학 점수를 입력하세요. >> '))
# num5 = int(input('역사 점수를 입력하세요. >> '))

for i in range(len(subject)):
  print(f'{subject[i]} : {score[i]}')
  sum += score[i]
print('합계 : ',sum)


# # 출력 함수
# def output():
#   print('과목')
#   print('-'*20)
#   for s in subject:
#     print(s)

# while True:
#   print('[과목 생성 프로그램]')
#   s_input = input('원하는 과목을 입력하세요. >> ')
#   subject.append(s_input)

#   output() # 출력함수호출

# 전역변수
# a = 10

# 함수 선언
# def func(a):
#   print(a)
#   a += 50
#   return a
#   # global a   # 전역변수를 가져옴
#   # # a = 50   # 지역 변수 : 함수를 종료하면 모두 제거됨
#   # print(a)
#   # a+=50
 
# # 함수 호출
# a = func(a)
# print(a)


a = 10
b = 20
c = 30
sum = 0

# def add(a,b):
#   return a+b

# sum = add(a,b) # 함수 호출
# print('합계 : ',sum)

# a에 함수를 사용해서, a+b+c의 합을 입력해서 출력 a에 저장

def add(a,b,c):  # 함수 내에 다시 선언된 변수 (지역변수)
  return a+b+c

a = add(a,b,c)
print(a)