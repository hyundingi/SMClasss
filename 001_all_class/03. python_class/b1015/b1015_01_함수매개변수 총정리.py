# 디폴트의 이해
print(1,2,3,4,5)          # 출력값 : 1 2 3 4 5
print(1,2,3,4,5, sep="")  # 출력값 : 12345

# 함수 - 기본매개변수, 가변매개변수, 키워드매개변수
# 매개변수 :: 함수의 괄호 안에 들어가는 것 (아래의 st, end 같은 것) -- 개수가 맞지 않으면 에러남~

# ----- 가변 매개 변수, 키워드 매개 변수 동시 사용할 경우
# 키워드 매개 변수는 가변 매개 변수 뒤로 와야함. ( 순서 : 기본 > 가변 > 키워드 )
def plus(*n, k=10):   # (k=10, *n) 의 순서로 넣으면 에러 혹은 값이 1이 됨
  print('k : ', k)
  for i in n:
    print(i)

plus(1,2,3,4,5)

# ----- 1. 기본 매개 변수 ----------
# def plus(n1, n2):
#   sum = n1+n2
#   return sum     # sum 값을 외부로 보내줌 (return)

# def plus(n1, n2):
#   sum = n1+n2
#   print('합계 : ',sum)

# # 함수 호출 -- 매개변수 개수를 정확히 맞추지 않으면 에러남~
# plus(10,20)


# ----- 2. 가변 매개 변수 ----------
# 기본 매개 변수를 같이 사용하려면, 가변 매개 변수 앞에 사용해야함.
# def plus(a, *n1, b):   # 리스트 형식으로 받기 때문에 매개 변수의 개수와 상관없이 받을 수 있따 (가변)
#   print('a : ' , a)   # 출력값 : [a :  1]
#   # print('b : ', b)    # 에러 :: *n1이 a에 할당하고 나머지를 다 받았기 때문에 에러남
#   for i in n1:
#     print(i)
#   print(type(n1))   # 튜플타입 [튜플]: 수정이 불가능한 리스트 타입

# plus(1,2,3,4,5)


# ----- 3. 키워드 매개 변수 ----------
# 매개 변수 개수가 일치하지 않으면 에러가 났으나, 키워드 매개 변수는 상관 없음. 
#  >> 함수 선언에 할당된 키워드 매개 변수가 디폴트 값이 되어주기 때문
# def plus(k=10, m=5):
#   print('k : ', k)
#   print('m : ', m)

# plus()            # 출력값 : k : 10    m : 5
# plus(1,2)         # 출력값 : k : 1    m : 2
# plus(m=10,k=2)    # 출력값 : k : 2    m : 10


# # ----------구구단-----------
# # 함수 선언
# def calc(st, end):
#   for i in range(st,end+1):
#     print(f'[{i}단]')
#     for j in range(1,9+1):
#       print(f'{i} * {j} = {i*j}') 


# # 2-9단
# # st = 2
# # end = 9
# # for i in range(st,end+1):
# #   print(f'[{i}단]')
# #   for j in range(1,9+1):
# #     print(f'{i} * {j} = {i*j}') 
# calc(2,9)   # 함수 호출

# #3-7단
# # st = 3
# # end = 7
# # for i in range(st,end+1):
# #   print(f'[{i}단]')
# #   for j in range(1,9+1):
# #     print(f'{i} * {j} = {i*j}') 
# calc(3,7)    # 함수 호출


# #5-9단
# # st = 5
# # end = 9
# # for i in range(st,end+1):
# #   print(f'[{i}단]')
# #   for j in range(1,9+1):
# #     print(f'{i} * {j} = {i*j}') 
# calc(5,9)     # 함수 호출

