import random

# 25개 1차원리스트
# 25개 중 1 5개 나머지는 0으로 입력해서 출력
a_list = []

# 1번 방법
a_list = [0]*20+[1]*5
random.shuffle(a_list)
print(a_list)

# 2번 방법
# for i in range(25):
#   if i<5:
#     a_list.append(1)
#   else:
#     a_list.append(0)
# print(a_list)



#### 5,5 2차원 리스트에 a_list의 값을 입력한 후 출력
b_list = []

# 2차원 리스트로 변환하기 1번 
# for i in range(5):
#   a = []
#   for j in range(5):
#     a.append(a_list[5*i+j])      # a_list 5개를 리스트에 추가
#   b_list.append(a)  # a_list 묶음(5개)을 b_list에 추가

# 2차원 리스트로 변환하기 2번 
for i in range(0,len(a_list),5):
  b_list.append(a_list[i:i+5])
print(b_list)


# 5*5  표 출력 후 좌표를 입력 받아 출력
while True:
  print('\t0\t1\t2\t3\t4')
  print('-'*50)
  for i in range(5):
    print(i, end='\t')
    for j in range(5):
      print(b_list[i][j], end='\t')
    print()
  input1 = input('좌표 입력')
  input2 = input1.split(',')
  print(f'{input1}의 값 : ', b_list[int(input2[0])][int(input2[1])])