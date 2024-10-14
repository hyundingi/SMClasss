# 두 수를 입력받아 더하기 출력
def plus(n1, n2):
  result = n1+n2
  return result

n1 = int(input('숫자1 >> '))
n2 = int(input('숫자2 >> '))
print(plus(n1,n2))
# print(plus(int(input('숫자1 >> ')),int(input('숫자2 >> '))))


# def plus(n1, n2):
#   result = n1+n2
#   return result

# # def plus2(n1, n2):
# #   return n1+n2

# print(plus(1,2))
# print(plus(55,45))
# print(plus(50,50))


# 2-50까지 3-7까지 5-50까지 / 사이의 값을 모두 더해서 출력
# def num_sum(st, end):
#   sum = 0
#   for i in range(st, end+1):
#     sum += i
#   return sum

# print('2-50까지의 합 : {:,d}'.format(num_sum(2,50)))
# print(f'3-7까지의 합 : {num_sum(3,7):,d}')
# print(f'5-50까지의 합 : {num_sum(5,50):,d}')
# total = num_sum(2,50) + num_sum(3,7) + num_sum(5,50)
# 출력값 : 합계 : 2,564
# print('합계 : {:,d} '.format(total))  # :,d 1000자리 구분 기호 

# def num_sum(st, end):
#   sum = 0
#   for i in range(st, end):
#     sum += i
#   return sum

# num1 = int(input('숫자를 입력하세요. >> '))
# num2 = int(input('숫자를 입력하세요. >> '))
# # print(num_sum(num1, num2))  # 호출한 곳으로 값을 되돌려줌 (return)

# num_sum(1,10)
# num_sum(1,100)
# total = num_sum(1,10)+num_sum(1,100)

# # 1-10 까지 합과 1-100까지의 합의 합을 출력
# print('합계 : ', total)
# print('프로그램 종료')


# def num_sum(st, end):   # (매개변수, 매개변수)
#   sum = 0
#   for i in range(st, end+1):
#     sum += i
#   print('합계 : ', sum)


# # 두 수를 입력받아, 그 사이의 숫자 합을 구하시오.
# # num1, num2 // 함수를 사용해서 계산하시오
# num1 = int(input('숫자1을 입력하세요. >> '))
# num2 = int(input('숫자2을 입력하세요. >> '))
# num_sum(num1, num2)


# # 1-10까지 합계 출력
# num_sum(1,10)

# sum = 0
# # 1-100까지 합계 출력
# num_sum(1,100)

# # 2-50까지 합계 출력
# num_sum(2,50)


# # 100-1000까지 합계 출력
# num_sum(100,1000)
