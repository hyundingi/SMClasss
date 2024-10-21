# --------- 기본 매개 변수 --------
# 1-1)
# def plus():
#   a = 50
#   print('지역변수 a : ', a)  # 50

# a = 10
# plus()
# print('전역변수 a : ', a)   # 10

# 1-2)
# def plus(a):
#   a += 50
#   print('지역변수 a : ', a)  # 60

# a = 10
# plus(a)
# print('전역변수 a : ', a)   # 10

# ----- return 값을 전달해야 값이 적용됨
# 2-1)
# def plus(a):
#   a = 50
#   print('지역변수 a : ', a)  # 50
#   return a

# a = 10
# a = plus(a)    
# print('전역변수 a : ', a)   # 10

# 2-2)
# def plus(a):
#   a += 50
#   print('지역변수 a : ', a)  # 60
#   return a

# a = 10
# a = plus(a)
# print('전역변수 a : ', a)   # 60


# -------- 복합 매개 변수 -----
def plus(a):
  a[0] = 100
  a[1] = 200
  print('지역변수 a : ', a)  # [100, 200]

a = [10,20]
plus(a)
print('전역변수 a : ', a)   # [100, 200]


