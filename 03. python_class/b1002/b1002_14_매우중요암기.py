import random

# 1-100까지의 랜덤숫자를 생성
# 입력한 숫자가 랜덤숫자보다 크면 입력한 숫자가 큽니다.
# 입력한 숫자가 랜덤숫자보다 작으면 입력한 숫자가 작습니다.
# 10번 도전하도록 하시오

r_num = random.randint(1,100)
count = 0

#### for문 사용
for a in range(10):
  count += 1
  num = int(input("1-100 중 숫자 한개를 입력하세요."))
  if r_num > num:
    print("입력한 숫자가 랜덤숫자보다 작습니다.")
  elif r_num == num:
    print('정답입니다. 정답번호 : ', r_num)
    break
  else:
    print("입력한 숫자가 랜덤숫자보다 큽니다.")
  if count == 10:
    print('게임오버 정답 번호 : ', r_num)

### while문 사용 (1)
# while True:
#   num = int(input("1-100 중 숫자 한개를 입력하세요."))
#   count += 1
#   if r_num > num:
#     print("입력한 숫자가 랜덤숫자보다 작습니다.")
#   elif r_num == num:
#     print('정답입니다. 정답번호 : ', r_num)
#     break
#   else:
#     print("입력한 숫자가 랜덤숫자보다 큽니다.")
#   if count == 10:
#     print('게임오버 정답 번호 : ', r_num)
#     break

### while문 사용 (2)
# while count<10:
#   num = int(input("1-100 중 숫자 한개를 입력하세요."))
#   count += 1
#   if r_num > num:
#     print("입력한 숫자가 랜덤숫자보다 작습니다.")
#   elif r_num == num:
#     print('정답입니다. 정답번호 : ', r_num)
#     break
#   else:
#     print("입력한 숫자가 랜덤숫자보다 큽니다.")
#   if count == 10:
#     print('게임오버 정답 : ', r_num)
#     break
  