# stu_data = ['홍길동', 100, 100, 100, 99]

# for s in stu_data:
#   print(s)


###### 값 한줄로 넣기
stu_title = ['번호', '이름', '국어', '영어', '수학', '과학', '합계', '평균']
stu_datas = [
  [1, '유관순', 100, 100, 100, 99],
  [2, '이순신', 100, 99, 98, 99],
  [3, '김구', 80, 100, 90, 99]
  ]

#### title 넣기 1번 
# print("                    [학생성적 프로그램]")
# print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(stu_title[0],stu_title[1],stu_title[2],stu_title[3],stu_title[4],stu_title[5],stu_title[6],stu_title[7]))
# print("-"*60)

#### title 넣기 2번
print("                    [학생성적 프로그램]")
for s_t in stu_title:
  print("{}".format(s_t), end = '\t') 
  # print("{}\t".format(s_t)) # 디폴트값 ,end = '\n' (줄바꿈)
print()
print("-"*60)

# 학번, 학생이름, 국어, 영어, 수학, 과학, 합계, 평균

for s in stu_datas:
  #print(s)
  print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(s[0],s[1],s[2],s[3],s[4],s[5],
                                                s[2]+s[3]+s[4]+s[5],
                                                (s[2]+s[3]+s[4]+s[5])/4))
  

# stu_total = stu_data[1] + stu_data[2] + stu_data[3] + stu_data[4]
# stu_avg = stu_total/4
# print(f"학생이름 : {stu_data[0]} \n 국어 : {stu_data[1]} \n 영어 : {stu_data[2]} \n 수학 : {stu_data[3]} \n 과학 : {stu_data[4]} \n 합계 : {stu_total} \n 평균 : {stu_avg} \n ")

# 이순신의 평균 출력
# print("이순신 평균 : ", (stu_datas[1][1]+stu_datas[1][2]+stu_datas[1][3]+stu_datas[1][4])/4) 




# 2개의 길이를 입력받아, 삼각형의 넓이, 직사각형의 넓이를 구하시오.

# num1 = int(input("길이 1 : "))
# num2 = int(input("길이 2 : "))

# print("삼각형의 넓이 : ", num1*num2*0.5)
# print("직사각형의 넓이 : ", num1*num2)

# 한번에 2개의 길이 입력받아 구하기
# length = input("2개의 길이 입력 : ")
# print(length.split(" "))

# length_list = length.split(" ")
# print ("삼각형의 넓이 : {}". format(float(length_list[0]) * float(length_list[1])*0.5))
# print ("직사각형의 넓이 : {}". format(float(length_list[0]) * float(length_list[1])))


# 원의 넓이 : 반지름 * 반지름 * 3.14
# 반지름을 입력받아, 원의 넓이를 구하시오

# a = int(input("반지름 입력 : "))
# area = a**2*3.14
# print("원의 넓이 : ", a**2*3.14)
# print("원의 넓이 : {:.1f}" .format(area))



# ### 복합대입연산자 
# # +=, -=, *=, /=, //=, %=, **=
# a = 10
# a += 5; print(a)
# a -= 5; print(a)
# a *= 5; print(a)
# a /= 5; print(a)
# a //= 5; print(a)
# a %= 5; print(a)
# a **= 5; print(a)


# ### 숫자를 문자열로 변환 
# # 문자열 + 숫자 : 불가능
# a = 100
# b = 10
# print(str(a)+str(b))


# a = "100"
# b = "10.5"
# c = "안녕"
# print(float(a)) # 정수형 > 정수타입, 실수타입 으로 변경 가능
# # print(int(b)) # 실수형 > 실수 타입으로만 변경 가능
# print(float(c)) # 글자는 숫자형 타입으로 변경 불가

# 여러줄 방정식을 1줄로 표현
# a = 10 ; b = 5
# s1, s2, s3 = 1, 2, 3


# 방정식?
# x = 1~10
# 1
# x = 11~20
# 11
# ,
# ,


# 특정숫자 a = 0, 1, 2, 3, 4, 5
# 1, 3, 5, 7, 9 > 2x+1

#### 우선 순위
# print(2 + 2 - 2 * 2 / 2 * 2)
# print(2 + (2 - (((2 * 2) / 2) * 2)))


# a = 5; b = 3 # 한 줄 형태로 쓸 경우 가운데 ; 넣어주면 됨

# # /, %, //, **
# print("나누기 : {}, 나머지 : {}, 정수 몫 : {}, 제곱 : {}" .format(a / b, a % b, a // b, a ** b ))
