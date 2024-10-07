import random

# 1-25 랜덤의 숫자 25개 중복없이 추출해서 
# (5,5)2차원 리스트에 입력해서 출력
a_list = []
b_list = []

# while len(a_list)<25:
#   num = random.randint(1,25)
#   if num not in a_list:
#     a_list.append(num)

# for i in range(5):
#   a = []
#   for j in range(5):
#     a.append(a_list[5*i+j])
#   b_list.append(a)
# print(b_list)

for i in range(25):
  a_list.append(i+1)
print(a_list)
random.shuffle(a_list) # 순서를 랜덤으로 바꿈
print(a_list)

# 0부터 25까지 5씩 증가
for i in range(0,len(a_list),5):
  b_list.append(a_list[i:i+5])
print(b_list)

# b_list 랜덤으로 섞어서 1-25까지 5,5 2차원리스트
while True:
  print('\t0\t1\t2\t3\t4')
  print('-'*50)
  for i in range(5):
    print(i,end='\t')
    for j in range(5):
      print(b_list[i][j], end='\t')
    print()
  input1 = input("좌표를 입력하세요. \n ex) [0,1] >> ")
  input2 = input1.split(',')
  print(f'{input1} 좌표의 값 : ', b_list[int(input2[0])][int(input2[1])])