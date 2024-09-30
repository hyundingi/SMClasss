# # 두 수를 입력받아 더하기 빼기 곱하기 나누기 출력

# num1 = int(input(" 숫자 1 입력 : "))
# num2 = int(input(" 숫자 2 입력 : "))

# print(" 더하기 : {} \n 빼기 : {} \n 곱하기 : {} \n 나누기 : {} \n" .format(num1+num2, num1-num2, num1*num2, num1/num2))
# print(f" 더하기 : {num1+num2} \n 빼기 : {num1-num2} \n 곱하기 : {num1*num2} \n 나누기 : {num1/num2} \n" )


### for 구문 찍먹
# a = 0
# for i in range(10): # ==(0,10) 0~9까지
#   a = a + i  
#   # a += i 로 변경 가능
#   print(a)


### 사칙연산 수식
# +, -, *, / - 몫(소수점 있음), % - 나머지 값, // - 정수형태 몫 (소수점 없음), ** (제곱)
# print(5+2) 
# print(5-2) 
# print(5*2) 
# print(5/2) # 2.5 (몫)
# print(5%2) 
# print(5//2) # 2 (몫의 정수)
# print(5**2) # 25 (제곱)
# print(3**3)


### 불형
# a = (10>100)
# print(a)

# b = (10==10)
# print(b)
# print(type(b))


### 문자형
# print("안녕 영어로는 \"hello\" 입니다") # 방법 1
# print('안녕 영어로는 "hello" 입니다') # 방법 2

## 자바스크립트 함수선언 
# function add(){
# var i = 0; // 지역변수
# }
### 파이선 함수 선언

b = 0 # 전역변수 선언
def add():
  print(10+9)
  a = 10 # 지역변수 선언 (함수를 벗어나면 선언이 안 먹힘)