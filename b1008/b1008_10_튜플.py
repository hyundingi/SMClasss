
a = ((1,2),(3,4),(5,6))
print(a[0])      # 출력값 : (1,2)
print(a[0][1])   # 출력값 : 2



# 문자열을 tuple 혹은 list 타입으로 변경 가능
# a_str = 'abcde'
# print(a_str)
# print(a_str[1])

# a_tu = tuple(a_str)
# print(a_tu)            # 출력값 : ('a', 'b', 'c', 'd', 'e')
# print(list(a_tu))      # 출력값 : ['a', 'b', 'c', 'd', 'e']
 

# 두 수의 치환
# a = '우유'
# b = '커피'
# c = ''
# print(a,b)

# 파이썬 a,b 치환
# a, b = b, a
# print(a,b)

# 기본적인 a,b 치환
# c = a
# a = b
# b = c
# print(a,b)



# 3차원 리스트 > 1차원 리스트
# aArr = [[1,2],[[1,2],[3,4]],[5,6],[7,8]]
# a_list = [1,2,3,4,5,6,7,8]
# b_list = []

# for i in aArr:
#   if type(i) == list:
#     for j in i:
#       if type(j) == list:
#         for k in j:
#           b_list.append(k)
#       else:
#         b_list.append(j)

# print(b_list)

# 2차원 리스트 >> 1차원 리스트
# aArr = [[1,2],[3,4],[5,6],[7,8]]
# a_list = [1,2,3,4,5,6,7,8]
# b_list = []

# for i in aArr:
#   if type(i) == list:
#     for j in i:
#       b_list.append(j)
# print(b_list)



# t = (1,2,3,4)
# print(type(t))


# 리스트 - 원본에 거의 반영이 안됨
# t = [3,5,1,2]
# t.sort()    # t리스트에 반영
# print(t)

# t[1:3]           # t변경되지않음
# print(t+[3,7])   # t에 반영 안 됨
# print(t)

# t.extend([3,7])  # t에 반영이 됨
# print(t)


# # 튜플 - 형태는 리스트 타입과 같음 
# # 수정 및 추가 안 됨
# t = (1,2,3,4)  
# # t[0] = 5      # 에러 (수정 불가)
# # t.append(100) # 에러 (추가 불가)


# # 더하기 연산자로 추가 가능
# t = t+(3,5)     
# print(t)

# # 곱하기 연산자 가능
# tt = (1,2,3)
# tt = tt*2
# print(tt)         # 출력값 : (1,2,3,1,2,3)

# # len() 함수 사용 가능
# print(len(t))


# # 출력 부분에는 문제가 안 됨
# for i in t:
#   print(i)

# tArr = [1,2,3,4]
# tArr[0] = 100
# print(tArr)