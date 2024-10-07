numbers = [273,103,5,32,65,9,72,800,99]

# 100 이상의 값만 출력
# for i in numbers:
#   if i > 100:
#     print(i)

# 순차정렬 - 낮은 수 부터 출력
# numbers.sort() 
# print(numbers)

# 역순정렬 - 높은 수 부터 출력
# numbers.sort(reverse=True) 
# print(numbers)
  
# 순서 역순 출력
print(numbers)
numbers.reverse()
print(numbers)     # 출력값 : [99, 800, 72, 9, 65, 32, 5, 103, 273]
