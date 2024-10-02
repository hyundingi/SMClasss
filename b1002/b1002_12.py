import random

# 랜덤숫자 생성 - random
# random() : 0 <= x < 1 실수값 추출
print(random.random())
# 0-9
print(int(random.random()*10))
# 1-10
print(int(random.random()*10)+1)


# 랜덤 int 추출 - 1~3까지 (3포함)
print(random.randint(1,3))

# 랜덤 범위 추출 - 1~2까지
print(random.randrange(1,3))

# 리스트에서 랜덤 추출
a = [1,4,5,9]
print(random.choice(a))

# 리스트에서 여러개 랜덤 추출 (중복 가능)
print(random.choices(a, k=2))

# 리스트에서 여러개 랜덤 추출 (중복 불가능)
print(random.sample(a,2))