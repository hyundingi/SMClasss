import random

# 랜덤 숫자 정수 1-100 생성
random.randint(1,100)


# 10번 도전
# 입력한 숫자가 더 크면 작은 수를 입력하셔야합니다.
# 10번 도전에서 못 맞추면 도전 실패

randnum = random.randint(1,100)
count = 0
while count<10:
  innum = int(input("1-100 숫자를 입력해보세요 "))
  count += 1
  if randnum > innum:
    print(count,"번째 도전! 입력하신 숫자가 랜덤 숫자보다 작습니다.")
  elif randnum < innum:
    print(count, "번째 도전! 입력하신 숫자가 랜덤 숫자보다 큽니다.")
  elif randnum == innum:
    print(count, "번재 도전! 정답입니다 ~~~~~ \n 랜덤 숫자 : ", randnum)
    break
  if count == 10:
    print("10번 도전에 실패했습니다. 랜덤 숫자 :", randnum)
    break
