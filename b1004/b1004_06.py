


# ~님 으로 다시 저장
a_list = ['홍길동', '유관순', '이순신']

a_list = [a+"님" for a in a_list]
print(a_list)



# a_list = [1,2,3,4,5]
# b_list = [1*1, 2*2, 3*3, 4*4, 5*5]

# print(a_list)
# 리스트의 값을 변경해서 리스트에 저장
# for idx, a in enumerate(a_list):
#   a_list[idx] = a*a #a**2

# 리스트의 값을 변경해서 리스트에 저장 - 리스트 내포(한줄 for문)
# 위의 for 문을 한줄로 나타낸 것임.
# a_list = [a*a for a in a_list]
# print(a_list)

# 리스트 값 변경
# a_list[1] = 100
# print(a_list)

# 없는 list 위치를 출력하면 에러
# a_list[5] = 1000
# print(a_list)

# 범위에 없는 값을 출력하려고 하면 에러
# print(a_list[10])

# 리스트 슬라이싱 0부터 3번까지 출력됨
# print(a_list[0:4])

# 리스트 범위보다 많이 출력 :: 에러는 안 나지만 출력은 됨(범위까지만)
# print(a_list[0:10])



# enumerate() 함수
# a_list = ['홍길동', '유관순', '이순신', '강감찬', '김구', '김유신', '홍길자']

# # for문으로 출력
# for a in a_list:
#   print(a)

# # enumerate()함수 - index 번호를 출력 index번호 , value
# for i,a in enumerate(a_list):
#   print(f"{i+1}:{a}")

# print(a_list)