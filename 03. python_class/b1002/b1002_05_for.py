
# 문자열 슬라이싱
# str = "좋은 하루되세요. 많은 행복받으세요. 많은 감사! 많은 돈."
# # 글자 길이수 확인
# print(len(str))

# # 뒤쪽에서 5자리 전까지 출력
# print(str[-5:]) # 출력값 : 많은 돈.
# print(str[-1]) # 출력값 : .
# print(str[::-1]) # 출력값 : .돈 은많 !사감 은많 .요세으받복행 은많 .요세되루하 은좋



# list 추가 - append (제일 뒤에 추가)/ insert (원하는 위치에 추가)
# list 삭제 - del (원하는 위치에 삭제) / remove (값으로 검색해서 삭제)
# a_list = [1,2,3]

# a_list.append(10)
# print(a_list)

# a_list.insert(2, 100)
# print(a_list)

# del a_list[1]
# print(a_list)

# a_list.remove(100)
# print(a_list)


students = [
  [1, '홍길동', 100, 90, 99],
  [2, '유관순', 100, 100, 99],
  [3, '이순신', 100, 100, 99]
]
print(len(students))
# 반복문
for i in range(10): # 0 부터 시작해서 10번 반복
  print(i, end="")

for i in range(2,5): # 2 ~ 4 반복 (5 이전까지)
  print(i)

for i in range (1, 10, 2): # 1부터 10이전까지 step2 해서 출력
  print(i, end="")

aArr = [1,2,5,7,8]
for i in aArr: # list의 값을 1개씩 가져와서 출력
  print(i, end="")


# enumerate :: index 번호를 추가해서 가져올 수 있음
for i, data in enumerate(aArr): # list의 값과 index번호를 함께 출력
  print(i, ":", data)

aStr = "안녕하세요"
for i in enumerate(aStr): # 문자열의 값을 1개씩 가져와서 출력
  print(i)

aStr = "안녕하세요"
for i in aStr: # 문자열의 값을 1개씩 가져와서 출력
  print(i)




# 번호 이름 국어 영어 수학
# s 리스트에 합계와 평균 추가
# s = [4, '강감찬', 100, 90, 99]
# s.append(s[2]+s[3]+s[4])
# print(s)
# s.append(round(((s[2]+s[3]+s[4])/3), 2))
# print(s)