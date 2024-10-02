# aArr = [2,3,4,6,7,8,9,10]

# # 50, 100 추가
# aArr.append(50)
# aArr.append(100)
# print(aArr)

# # 2번 자리에 30 추가
# aArr.insert(2, 30)
# print(aArr)

# # 숫자 6 삭제
# aArr.remove(6)
# print(aArr)

# # 첫번째, 네번째  데이터 삭제
# del aArr[3]
# del aArr[0]
# print(aArr)




# all_list = [
#   [1, '홍길동', 100],
#   [2, '유관순', 200],
#   [3, '이순신', 100]
# ]

# a = [3, '이순신', 100]

# all_list 에서 a 와 같은 거 삭제

# 1
# all_list.remove(a)
# print(all_list)

# 2
# for i in all_list:
#   if a == i:
#     all_list.remove(i)
#     print(all_list)




# all_list 에서 이름이 유관순 인 것을 삭제

# remove 로 지우기
# for i in all_list:
#   if i[1] == '유관순':
#     all_list.remove(i)
#     print(all_list)

# del 로 지우기 
# for idx, i in enumerate(all_list):
#   if i[1] == '유관순':
#     del all_list[idx]
#     print(i)
#     print(all_list)




students = [
  [1, '홍길동', 100, 90, 99],
  [1, '유관순', 100, 90, 99],
  [1, '이순신', 100, 90, 99],
  [1, '강감찬', 100, 90, 99],
  [1, '김구', 100, 90, 99]
]

# 이름을 입력받아 같은 이름이 있으면 삭제 / 없으면 없습니다 출력 

name = input("이름 입력 : ")
count = 0
for i in students:
  if i[1] == name:
    students.remove(i)
    count = 1
    print(f"{name}을 삭제합니다.")
    break
  
if count == 0:
  print("찾고자하는 이름이 없습니다.")

print(students)