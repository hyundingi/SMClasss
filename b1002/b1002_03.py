# 입력한 숫자가 짝수인지 홀수인지 출력
# a = int(input("숫자 입력 : "))

# if a%2 == 0:
#   print("짝수 입니다.")
# else:
#   print("홀수 입니다.")



# 입력한 숫자가 1보다 크고 10보다 작을 때만 정답입니다.
# a = int(input("숫자 입력 : "))

# if 1 <= a <= 10:
#   print("정답입니다.")
# else:
#   print("오답입니다.")


# 입력한 숫자가 10보다 작거나 100보다 클 때 정답입니다.
# a = int(input("숫자 입력 : "))

# if 10 <= a <= 100: # a <= or a>= 100
#   print("정답입니다.") 
# else:
#   print("오답입니다.")


# 3,4,5 봄 6,7,8 여름 9,10,11 가을 12,1,2 겨울
# a = int(input("숫자 입력"))

# if a == 3 or a == 4 or a ==5:
#   print(a, "월은 봄 입니다.")
# elif a == 6 or a == 7 or a == 8:
#   print(a, "월은 여름 입니다.")
# elif a == 9 or a == 10 or a == 11:
#   print(a, "월은 가을 입니다.")
# elif a == 12 or a == 1 or a == 2:
#   print(a, "월은 겨울 입니다.")
# else:
#   print("잘못된 월이 입력되었습니다.")


# 100~98 a+ / 97 ~ 94 a / 93 ~ 90 a- / 89, 88 b+ / 87~ 84 b / 83 ~ 80 b- / 60점 이하 f
a = int(input("점수 입력 : "))

if 98 <= a <= 100:
  print("A+ 입니다.")
elif 94 <= a <= 97:
  print("A 입니다.")
elif 90 <= a <= 93:
  print("A- 입니다.")
elif 88 <= a <= 89:
  print("B+ 입니다.")
elif 84 <= a <= 87:
  print("B 입니다.")
elif 80 <= a <= 83:
  print("B- 입니다.")
elif 77 <= a <= 79:
  print("C+ 입니다.")
elif 73 <= a <= 76:
  print("C 입니다.")
elif 70 <= a <= 72:
  print("C- 입니다.")
elif 67 <= a <= 69:
  print("D+ 입니다.")
elif 63 <= a <= 66:
  print("D 입니다.")
elif 60 <= a <= 62:
  print("D- 입니다.")
elif a < 60:
  print("F 입니다.")
else:
  print("올바른 점수를 입력하세요.")
