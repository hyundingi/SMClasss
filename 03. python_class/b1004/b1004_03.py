
# 0부터 1씩 증가하면서 10번 실행
for i in range(10):
  print(i)



# 5부터 9까지 1씩 증가하면서 실행
print ("-"*10)
for j in range(5,10):
  print(j)


print ("-"*10)
a_list = [1,2,3,4,5]
for k in a_list:
  print(k)


# 파이썬 - 문자열: str / 정수형: int/ 실수형: float/ 논리형: bool
# 리스트 타입 - []
print ("-"*10)
b_list = [3,5,9,10,20,3,3,10,5,20]
for m in b_list:
  print(m)      #b_list 의 요소를 하나씩 가져옴
  print(b_list) #b_list 의 개수번 만큼 가져옴


# 딕셔너리타입 - {} : json타입과 모양이 같음. 키, 값(key, value)
print ("-"*10)
dic = {
  "번호" : 1,
  "이름" : "홍길동",
  "국어" : 100,
  "영어" : 100,
  "수학" : 99
}
print("번호 :", dic["번호"])
print("이름 :",dic["이름"])

for n in dic: # dic 에서 key 값을 n에 넣어줌
  print(n) # key값이 출력이 됨.
  print(dic[n]) # key값의 value값이 출력이 됨.


#리스트의 길이 : len()
print ("-"*10)
print(len(b_list))


# 리스트 안에 해당 숫자가 몇개인지 확인
print ("-"*10)
print(b_list.count(5))


# 리스트에 추가 - append, insert, extend([2,3]):: 리스트를 추가
# 리스트에 삭제 - del, remove, clear (모두삭제)