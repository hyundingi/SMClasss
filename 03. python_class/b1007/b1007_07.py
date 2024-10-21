import random

a_list = [
  [0,1,0],
  [0,0,1],
  [1,0,0]
]

lotto = [0]*6+[1]*3
random.shuffle(lotto)

for i in range(3):
  for j in range(3):
    a_list[i][j] = lotto[3*i+j]


aa_list = [
  ['로또', '로또', '로또'],
  ['로또', '로또', '로또'],
  ['로또', '로또', '로또']
]

while True:
  my_money = int(input('얼마를 투자하시겠습니까? >> '))
  print('     [i][j] 좌표')
  print('\t0\t1\t2\t')
  print('-'*30)
  for i in range(3):
    print(i, end='\t')
    for j in range(3):
      print(aa_list[i][j], end='\t')
    print()

  code = input('좌표를 입력하세요. >> ' )
  codeArr = code.split(',')
  # print(f'{codeArr} 좌표값 : ', a_list[int(codeArr[0])][int(codeArr[1])])
  if a_list[int(codeArr[0])][int(codeArr[1])] == 1:
    print(f'{codeArr} 결과 : 당첨 \n {my_money*10:,d}원')
  else:
    print(f'{codeArr} 결과 : 꽝 \n 다음기회에')