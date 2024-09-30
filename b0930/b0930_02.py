# 10은 2의 배수 입니다.

a = 10
b = 2
# print(a+"은 "+b+"의 배수 입니다.")
print(a,b)

# 출력 자리수
print("%d" % b)
print("%5d" % b) # 공간 5자리 확보
print("%05d" % b)

# 001 010 100.00
num = 1
num2 = 10
num3 = 100
print("%03d" % num)
print("%03d" % num2)
print("%.2f" % num3)

print("%03d %03d %.2f" % (num, num2, num3))  

print("%5d" % (-10))

# print("숫자:"+10) :: 타입이 다른 것을 +할 수 없음
print("quiz 1번, 2번 : %.2f %010.2f" % (758.12345678, 25.05))
print("quiz 3번 : %d, %f, %s" % (150.15, 150.15, 150.15))
print("quiz 4번 : ", "*" * 10)

print("%5.1f" % (123456789.123)) # 출력값 : 123456789.1
 
# 10*2=20
# print("%d * %d = %d" % (a,b,a*b))

# 사용 표시 : %d - 정수 || %f - 소수점(실수) || %c - 문자 1개 || %s - 문자열
# 홍길동 총합 : 299, 평균 : 99.3333
# name = "홍길동"
# kor = 100
# eng = 100
# math = 99
# print("%s 총합 : %d, 평균 : %f" % (name, kor+eng+math, (kor+eng+math)/3))


### 프린트 사용 형태
#print -- 쉼표, %, .format, f
# print(a, "은", b, "의 배수 입니다.")
# print("%d는 %d의 배수 입니다." % (10,2))
# print("{}은 {}의 배수입니다." .format(a, b))
# print(f"{a}은 {b}의 배수입니다.")