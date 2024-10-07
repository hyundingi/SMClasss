import random

lotto = [0]*6+[1]*3
random.shuffle(lotto)
a_list = []
hidden = [
  [' - ', ' - ', ' - '],
  [' - ', ' - ', ' - '],
  [' - ', ' - ', ' - ']
]

for i in range(3):
  a = []
  a_list.append(a)
  for j in range(3):
    a.append(lotto[i*3+j])

while True:
  money = int(input('얼마를 투자하시겠습니까?'))
  print('        좌표')
  print('\t0\t1\t2')
  print('-'*30)
  for i in range(3):
    print(f'{i}|', end='\t')
    for j in range(3):
      print(hidden[i][j], end='\t')
    print()
  
  input1 = input('좌표를 입력하시오 >> ')
  input2 = input1.split(',')
  print(f'{input1}의 결과 : ', a_list[int(input2[0])][int(input2[1])])
  if a_list[int(input2[0])][int(input2[1])] == 0:
    print('꽝입니다. 다음기회에.')
  else:
    print(f'축하합니다. 당첨! \n 당신의 당첨금 :{money*10:,d}')


