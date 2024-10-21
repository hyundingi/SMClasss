import random


r_num = random.randint(1,100)
count = 0
# while count < 10:
#   num = int(input("1에서 100중 숫자 하나를 입력하세요."))
#   count += 1
#   if num > r_num:
#     print(f'입력한 숫자가 랜덤 숫자보다 큽니다. ({count}번째 도전)')
#   elif num < r_num:
#     print(f'입력한 숫자가 랜덤 숫자보다 작습니다. ({count}번째 도전)')
#   else:
#     print(f'정답입니다. \n 도전 횟수 : {count} \n 정답 : {r_num}')
#     break
#   if count == 10:
#     print('게임오버 정답 : ', r_num)


for a in range(10):
  num = int(input("1에서 100중 숫자 하나를 입력하세요."))
  count += 1
  if num > r_num:
    print(f'입력한 숫자가 랜덤 숫자보다 큽니다. ({count}번째 도전)')
  elif num < r_num:
    print(f'입력한 숫자가 랜덤 숫자보다 작습니다. ({count}번째 도전)')
  else:
    print(f'정답입니다. \n 도전 횟수 : {count} \n 정답 : {r_num}')
    break
  if count == 10:
    print('게임오버 정답 : ', r_num)
