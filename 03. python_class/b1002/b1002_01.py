# input_str = input("글자를 입력하세요.")

# 문자가 입력되지 않았을 때
# if input_str == "":
#   print("글자를 입력하셔야 합니다.")
# else:
#   print("입력문자 : ", input_str)

# 문자가 입력되었을 때
# if input_str != "":
#   print("입력문자 : ", input_str)
# else:
#   print("글자를 입력하셔야 합니다.")


# 문자열
a = "123"
print(type(a))
print(type(int(a)))
print(type(float(a)))

b = "12.3"
# print(type(int(b))) #에러남
print(type(float(b))) # 소수점이 있는 문자열 숫자는 꼭 float으로 변경해야함

c = 12.3
print(type(int(c))) # 숫자는 int 타입으로 변경  가능 
print(int(c))

s1 = "안녕"
s2 = "하세요"

print(s1+s2)
print(a+b) # 문자열 연결연산자
# print(a*b) # 에러남 : 문자열은 -,*,/ 안됨

# 문자열 *n :: 문자열 반복 연산자 (문자열에 곱하기는 숫자만 가능임)
print(s1*10)

# 문자열 슬라이싱
str1 = "안녕하세요 반갑습니다." # 문자열 자체를 리스트(배열) 형태로 봄
print(str1[0]) # 출력값 : 안
print(str1[2:5]) # 출력값 : 하세요 (범위를 지정하여 출력)
print(str1[:5]) # 출력값 : 안녕하세요 (범위 : ~[4] 까지 출력)
print(str1[6:]) # 출력값 : 반갑습니다. (범위 : [6]~ 부터 출력)
print(str1[1:10:2]) #출력값 : 녕세 갑니 (1~10까지 중 2개간격으로 출력)
print(str1[1:10:3]) #녕요갑
print(str1[::-1]) # [처음부터 : 끝까지 : 역순으로]

# [] - 배열 : 한 번 범위가 정해지면 수정이 불가능  -- c, 자바 
# [] - 리스트 (파이썬) : 범위 상관 없음.