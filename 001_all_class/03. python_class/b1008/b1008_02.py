# 1차원 리스트 > 2차원 리스트 [4,5]
aArr = []
for i in range(20):
  aArr.append(3*i)
print(aArr)

a_list = []
for j in range(4):
  a = []
  a_list.append(a)
  for k in range(5):
    a.append(aArr[5*j+k])
print(a_list)




# [4,5] 2차원 리스트
# alist = []
# for i in range(5):
#   a = []
#   alist.append(a)
#   for j in range(5):
#     a.append(i*5*3+(j*3))
#     print(alist[i][j], end = '\t')
#   print()

