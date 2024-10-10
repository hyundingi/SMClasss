# 3. 숫자맞추기게임 (로또)
# 구현
# b1002 > b1002_14.py
# * 내가 입력한 숫자를 리스트에 저장까지

import random


r_num = random.randint(1,100)
count = 0
numlist = []

for a in range(10):
  count += 1
  num = int(input(f'{count}번째 도전) 숫자를 입력하세요. >> '))
  numlist.append(num)
  if num > r_num:
    print('입력한 숫자가 랜덤숫자보다 큽니다. 작은 수를 입력하세요.')
    print(f'현재까지 입력한 숫자 : {numlist}')
  elif num < r_num:
    print('입력한 숫자가 랜덤숫자보다 작습니다. 큰 수를 입력하세요.')
    print(f'현재까지 입력한 숫자 : {numlist}')
  elif num == r_num:
    print(f'축하합니다. 정답입니다. \n 정답 : {r_num}')
    print(f'현재까지 입력한 숫자 : {numlist}')
    break
