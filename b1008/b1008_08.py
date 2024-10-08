# 얕은 복사, 깊은 복사
name = ['홍길동','유관순','이순신']
score = [100,90,95]
n_dic = dict(zip(name, score))
print(n_dic)

a = n_dic # 얕은 복사
a['홍길동'] = 0
print(a)
print(n_dic)

import copy
a = copy.deepcopy(n_dic)  # 깊은 복사




# 리스트 타입 / 얕은 복사 깊은 복사 /
# name = ['홍길동','유관순','이순신']
# score = [100,90,95]

# 얕은 복사
# n의 이순신 > 김구로 변경 :: name의 이순신도 김구로 변경됨
# n = name     # name의 값을 n에 복사
# n[2] = '김구'
# print(n)
# print(name)


# 깊은 복사
# n의 이순신만 김구로 변경됨 !!!
# n = name[:] # n이 새로운 주소값으로 저장됨
# n[2] = '김구'
# print(n)
# print(name)
