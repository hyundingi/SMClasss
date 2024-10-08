# 25개 1차원 리스트 생성 > 1~25 까지 입력한 후 랜덤으로 다시 출력
# 5,5 2차원 리스트 생성

import random
aArr = []
for i in range(25):
  aArr.append(i+1)
print(aArr)
random.shuffle(aArr)
print(aArr)

a_list = []

print('\t0\t1\t2\t3\t4\t')
print('-'*50)
for i in range(5):
  a = []
  a_list.append(a)
  print(i, end ='\t')
  for j in range(5):
    a.append(aArr[5*i+j])
    print(a_list[i][j], end = '\t')
  print()

num = input('좌표를 입력하세요.')
num2 = num.split(',')
print(a_list[int(num2[0])][int(num2[1])])

# 값을 입력하면 해당 좌표 출력 
val = int(input('값을 입력하세요'))
for i in range(5):
  for j in range(5):
    if val == a_list[i][j]:
      print(f'좌표 값 :  {[i, j]}')
  




