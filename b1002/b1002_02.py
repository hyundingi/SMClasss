# a = 100
# if문  :을 넣음, if 안쪽은 들여쓰기 해야함
# if a>10:
#   print("10보다 큰 수 입니다.")
#   pass
### if문에는 1줄이 있어야 에러가 나지 않음

# 숫자를 입력받아 100ㅂ로다 큰 수인지 작은 수 인지 출력
a = int(input("숫자를 입력하세요."))

if a>100 :
  print("100보다 큰 수 입니다.")
elif a == 100:
  print("100 입니다.")
else:
  print("100보다 작은 수 입니다.")