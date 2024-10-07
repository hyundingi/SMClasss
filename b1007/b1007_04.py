import random

# 1,25 사이의 랜덤숫자 생성
# num1 = random.randint(1,25)
# num2 = int(random.random()*25)+1

# 1-25까지 랜덤숫자를 입력, 중복은 제거 
# 반복 25번
# 1번 (내가한 거)
a_list = []
# while True: 
#   randnum = random.randint(1,25)
#   a_list.append(randnum)
#   # print(a_list)
#   if a_list.count(randnum) > 1:
#     a_list.remove(randnum)
#   if len(a_list) == 25:
#     break
# print(a_list)
# print(len(a_list))

#2번 
# while len(a_list)<25:
#   num = random.randint(1,25)
#   if num not in a_list:
#     a_list.append(num)
# print(a_list)
# print(len(a_list))

# 3번 -- random.sample() : 범위 안에 수를 랜덤으로 추출하며 중복으로 추출 안됨
# for i in range(25):
#   a_list.append(i+1)
# b_list = random.sample(a_list, 25)
# print(b_list)

# 4번 -- random.choices() : 범위 안에 수를 랜덤으로 추출하지만 중복될 수 있음. 
for i in range(25):
  a_list.append(i+1)
b_list = random.choices(a_list,k=25)
print(b_list)