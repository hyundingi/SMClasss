# 2차원 리스트
 # for문을 2번 작성해서 1,25가지 5,5 리스트를 생성하시오
a_list = []
for i in range(0, 5):
  a = []
  a_list.append(a)
  for j in range(1,6):
    a.append(i*5+j)
print(a_list)




# a_list = [] # 0~ 8번 인덱스 
# for i in range(9):
#   a_list.append(i+1)
# print(a_list)

# b_list = []
# for i in range(9):
#   b = []
#   if a_list[i]%3 == 0:
#     b.append(a_list[i])
   

# [3,3] 리스트 [1,2,3],[4,5,6],[7,8,9]
# 1-9까지 for문을 사용해서, 2차원 리스트에 추가하시오
# a_list = []
# for i in range(0,3):
#   a = []
#   a_list.append(a)
#   for j in range(1,4):
#    a.append((3*i)+j)
# print(a_list)
    

# 1-9 까지 for문을 사용해서, 1차원리스트에 추가하시오
# b_list = []
# for i in range(1,10):
#   b_list.append(i)
# print(b_list)



# 2차원 리스트는 for 문을 두번씀
# a_list = [
# [1,2,3,4],
# [5,6,7,8],
# [9,10,11]
# ]
# for i in a_list:
#   for j in i:
#     print(j)
