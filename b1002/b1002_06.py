students = [
  [1, '홍길동', 100, 90, 99],
  [2, '유관순', 100, 100, 99],
  [3, '이순신', 100, 100, 99]
]

# for s in students: # 한번에 모두 출력
#   print(s)
# print(students) # 한개씩 가져와서 출력

# # 이름이 유관순 인것을 출력
# for s in students: # 한번에 모두 출력
#   if s[1] == "유관순":
#     print(s)
  
ss = [4, '강감찬', 100, 90, 99]

# students 에 ss 추가
students.append(ss)

# 이순신 데이터 삭제 (remove 사용)
# for i in students:
#   if i[1] == '이순신':
#     students.remove(i)
#     print(students)

for idx, i in enumerate(students):
  if i[1] == '이순신':
    del students[idx]
    print(students)
    print(i) # 출력값 : [3, '이순신', 100, 100, 99]
    print(idx) # 출력값 : 2
