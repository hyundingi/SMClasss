ss = '파이썬 수업중 타입 문자열,정수형,실수형,논리형 타입이 있습니다.'
# i_str = input('글자를 입력하세요. >> '

a_str = '파이썬'
a = '-'.join(a_str)
print(a)



# 1 ) print(ss.replace(' ',''))
# 2 ) sss = ss.replace(' ','')  print(sss)

# 입력한 값이 몇개있는지
# idx = ss.count(i_str)
# print('개수 : ', idx)

# 타입의 위치값을 모두 출력하시오.
# idx = 0
# a_list = []
# for i in range(ss.count(i_str)):
#   num = ss.find(i_str, idx)
#   a_list.append(num)
#   idx = num+1
# print(f'검색개수 : {len(a_list)} / 위치값 : {a_list}')

# 입력한 값이 어느 위치에 있는지
# find = 위치값 출력, 없으면 -1 출력
# idx = ss.find(i_str)
# print('위치값 : ', idx)
# index = 위치값 출력, 없으면 에러
# idx = ss.index(i_str)
# print('위치값 : ', idx)



# 입력한 값이 있는지 없는지
# if i_str in ss:
#   print('있습니다.')
# else:
#   print('없습니다.')




# # 1-20 중에 3의 배수만 리스트에 추가
# a_list = []
# for i in range(1,21):
#   if i%3 == 0:
#     a_list.append(i)
# print(a_list)

# # 리스트 내포 사용
# # [값 for문 조건식]
# b_list =  [i for i in range(1,21) if i%3 == 0]
# print(b_list)




# # 한줄 for문으로 a_list 에 aArr 제곱값 넣기
# aArr = [1,2,3,4,5]
# a_list = []
# a_list = [i*i for i in aArr]
# print(a_list)
