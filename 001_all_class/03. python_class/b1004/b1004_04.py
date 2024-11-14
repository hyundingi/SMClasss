# 두 수를 입력받아 범위 내 수의 합계
a = int(input("숫자 1 : "))
b = int(input("숫자 2 : "))

### 내가 한 방법
# sum = 0
# if a<b:
#   for c in range(a,b+1):
#     sum += c
#   print("합계 : ", sum)
# else:
#   for c in range(b,a+1):
#     sum += c
#   print("합계 : ", sum)

### 1번째 방법
# min_num = a ; max_num = b
# sum = 0
# if a> b:
#   min_num = b; max_num = a

# for c in range(min_num, max_num+1):
#   sum += c
# print("합계 : ", sum)

### 2번째 방법 (min, max 함수 사용)
# sum = 0
# for i in range(min(a,b),max(a,b)+1):
#   sum += i

# print("합계 :", sum)

### 3번째 방법 (파이썬만 가능 - 두개 변수 치환 // 다른 언어들은 변수 하나를 더 둬야 가능 )
# if a>b:
#   a,b = b,a

# sum = 0
# for i in range(a,b+1):
#   sum += i
# print("합계 :", sum)


#1,3,5,7,9 합계
# sum = 0
# for i in range(1,9+1,2):
#   sum += i
# print("합계 : ",sum)

# 1-100 까지 숫자의 합
# sum = 0
# for i in range(1,100):
#   sum += i
# print("합계 : ",sum)


# 0: 안녕하세요.
# 1: 안녕하세요.
# 2: 안녕하세요.
# for i in range(3):
#   print(i,": 안녕하세요")
#   print(f"{i}: 안녕하세요")


# 1 - 1번출력 / 2 - 2번출력 3- 3번출력
# for i in [1,2,3]:
#   print("안녕하세요.\n"*i, end="")
#   print("-"*20)


# for 문을 사용해서 * 출력
# 출력값
# *
# **
# ***
# ****
# *****
# for i in range(0,5+1):
#   print("*"*i)

# 출력값(역순)
# ******
# *****
# ****
# ***
# **
# *
# for ii in range(5+1,0,-1):
#   print("*"*ii)


# 구구단 1,3,5,7,9
# for i in range(1,9+1,2):
#   print(f"[{i}단]")
#   for j in range(1,9+1):
#     print(f"{i} x {j} = {i*j}")
#   print("-"*15)


# 구구단 출력
# for i in range(2,9+1):
#   print(f"[{i}단]")
#   for j in range(1,9+1):
#     print(f"{i} x {j} = {i*j}")
#   print("-"*10)


# 1,3,5,7,9 까지 출력
# for i in range(1,10,2):
#   print(i)


# 1-10 까지 for 문을 사용해서 출력
# for i in range(1,11):
#   print(i)