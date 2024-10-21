s_list = []
no = 1
while True:
  # 이름 국어 영어 수학 을 입력받아 + 합계 평균 출력
  name = input(" 이름 입력(종료: 0) : ")
  if name == '0':
    break
  kor = int(input(" 국어 점수 입력 : "))
  eng = int(input(" 국어 영어 입력 : "))
  math = int(input(" 국어 영어 입력 : "))
  print(f"번호 : {no}, 이름 : {name}, 국어 : {kor}, 영어 : {eng}, 수학 : {math}, 합계 : {kor+eng+math}, 평균 : {(kor+eng+math)/3:.2f}")

  no += 1
  

# 입력한 숫자를 계속 더하는 프로그램
# 0이 입력되면 프로그램 종료

# sum = 0
# while True:
#   a = int(input("숫자 입력 : "))
#   if a == 0:
#     break
#   sum += a
#   print("입력한 값의 합 : ", sum)


# break : 반복문 종료
# i = 0
# j = 0
# while i<10:
#   print("번호1 : ", i)
#   while j<10:
#     if j<10:
#       if j == 5:
#         break    # j의 반복문만 종료
#     print("번호2 : ", j)
#     j += 1


# 이 중 while문 i = 1,10 / j=1,10 - j 출력을 1,3,5,7,9

# i,j = 1,1
# while i<10:
#   while j<10:
#     if j % 2 != 0:
#       print(i,j)
#     j += 1
#   j = 1
#   i += 1

# i,j = 1,0
# while i<10:
#   while j<10:
#     j += 1
#     if j % 2 == 0:
#       continue  
#     print(i,j)
#   j = 0
#   i += 1


# 두 수를 입력받아 + - * /

# while True:
#   num = int(input("숫자 1 입력 : "))
#   num2 = int(input("숫자 2 입력 : "))

#   if num2 == 0:
#     break
  
#   print("[두 수의 사칙연산]")
#   print("-"*50)
#   print("1. 두 수 더하기")
#   print("2. 두 수 빼기")
#   print("3. 두 수 곱하기")
#   print("4. 두 수 나누기")
#   print("-"*50)
#   choice = int(input("원하는 번호를 입력하세요. >> "))

  
#   if choice == 1:
#     print("결과값 : ", num+num2)
#   elif choice == 2:
#     print("결과값 : ", num-num2)
#   elif choice == 3:
#     print("결과값 : ", num*num2)
#   elif choice == 4:
#     print("결과값 : ", num/num2)


# i = 0
# while True:   # 무한반복
#   print(i)
#   i += 1


# ## 구구단 출력
# i = 1
# while i<10:
#   j = 1
#   while j<10:
#     print(f"{i} x {j} = {i*j}")
#     j += 1
#   i += 1


# for i in range(1, 10):
#   for j in range(1, 10):
#     print(f"{i} x {j} = {i*j}")

# i = 0
# while(i<10):
#   print(i)
#   i += 1

# for i in range(10):
#   print(i)