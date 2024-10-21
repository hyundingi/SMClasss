a = 10 # 전역변수
def calc(a):
  a += 10
  print(a)
# 위와 같이 사용하면 됨

# def calc():
#   a += 10
#   print(a)   # 위에서 a를 활용하면 지역변수 내 a 에서 값을 찾으려고 함 (에러)

calc(a)


# 함수 - 매개변수 (일반변수, 복합변수)
# 3. 함수 복합매개변수 - return없이 함수 밖에서 값 사용 가능.
# def calc(hArr):
#   for i in range(len(hArr)):
#     hArr[i] += 100

# hArr = [1,2,3,4,5]  # 복합 변수 - 변수에 주소값이 저장됨.
# print(calc(hArr))  # 리스트와 같은 주소값에 함수 적용됨 - 하지만 return value 값이 없어서 출력값 : none
# calc(hArr)     # 리스트와 같은 주소값에 함수 적용됨
# print(hArr)    # 리스트 출력 (함수가 적용되어있음)

# 2. 전역변수 - 일반매개변수 return없이 함수 밖에서 값 사용 가능.
# def calc():
#   global h
#   h += 100

# # 위에서 h를 전역변수 선언 했기 때문에 아래에 있던 값이 위의 h 값으로 올라감
# # (함수 외부에 h 값이 정의되어 있다면 가져와서 씀)
# h = 20  
# calc()
# print(h)



# 1. 함수 일반매개변수 - return이 아니면 값이 함수 밖으로 나올 수 없음.
# def calc(hh):
#   hh += 100
#   return hh

# h =20
# calc(h)
# print(h)

# # 호출만 하고 일반변수 값을 넣어주지 않으면 값이 변경되지 않음.
# h = calc(h) 
# print(h)

# # 혹은 프린트 안에 호출해야 원하는 출력값이 나옴
# print(calc(h))
