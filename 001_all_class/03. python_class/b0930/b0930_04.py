var1 = 100
var2 = var1
var3 = var2
var4 = var3
print(var4)

v4 = v3 = v2 = v1 = 10
print(v4)

### 문자 타입 확인
# name = "홍길동"
# print(type(name))

# level = '3레벨'
# print(type(level))

# n = 3.14
# print(type(n))

# num = 100
# print(type(num))

# a_bool = True  #True False 대문자로 넣어야함!
# print(type(a_bool))

## 타입변경 - str, float, int, bool로 가능
# a = '100'
# print(type(a))

# b = '200'
# print(type(b))

# print(a+b) # 결과값 : 100200 //  문자 연결 연산자
# print(int(a)+int(b))

# c = '3.14' # 문자실수형은 실수형으로 변경 후 정수형으로 변경 가능 
# print(float(c))
# print(int(float(c)))
# print(str(c)) #실수 형을 문자열로 변경

# c1 = 3.14
# print(int(c1))

# d = "True"
# print(bool(d)) # 문자 불형을 불형으로 변경





# name, kor, eng, math, total, avg 출력
# input으로 입력받아
# 홓ㅇ길동, 100,100,99 합계 평균 1줄에 입력하시오
# format 함수 사용, f함수 사용

name = input("이름 입력 : ")
kor = input("국어 점수 입력 : ")
eng = input("영어 점수 입력 : ")
math = input("수학 점수 입력 : ")
total = int(kor)+int(eng)+int(math)
avg = total/3

print("이름 : {} \n 국어 점수 : {} \n 영어 점수 : {} \n 수학 점수 : {} \n 점수 총합 : {} \n 점수 평균 : {:.2f} \n " .format(name, kor, eng, math, total, avg))
print(f'이름 : {name} \n 국어 점수 : {kor} \n 영어 점수 : {eng} \n 수학 점수 : {math} \n 점수 총합 : {total} \n 점수 평균 : {round(avg, 2)} \n')