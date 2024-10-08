# 리스트타입
# 튜플 타입 - 수정 불가
# 딕셔너리

dic1 = {'번호':1, '이름':'홍길동', 'kor':100, 'eng':100}


print(dic1)

# 키만 출력 
# key()
# 타입변경
print(dic1.keys())  # 출력값 : dict_keys(['번호', '이름', 'kor', 'eng']) 
print(type(dic1.keys())) # type :: class 객체
# print(dic1.keys()[0]) # class 객체이기 때문에 index 값ㅇ ㅣ없음 
print(list(dic1.keys()))
print(list(dic1.keys())[0]) # 출력값 : 번호

# 키만 출력
for key in dic1:
  print(key)


# 값만 출력
for key in dic1:
  print(dic1[key])

# 값만 출력
# values() : class 타입
print(dic1.values())
print(list(dic1.values()))


# 키, 값 모두 출력
for key in dic1.keys():
  print(key, dic1[key])
  # 출력값
  # 번호 1
  # 이름 홍길동
  # kor 100
  # eng 100

# 키, 값을 모두 출력
print(dic1.items())        # 출력값 :  dict_items([('번호', 1), ('이름', '홍길동'), ('kor', 100), ('eng', 100)])
print(list(dic1.items()))  # 출력값 :  [('번호', 1), ('이름', '홍길동'), ('kor', 100), ('eng', 100)]


# 출력 방법 : 키를 입력하면 값을 출력
print(dic1['이름']) # 출력값 : 홍길동
# print(dic1['학번']) # 에러 (없는 키 값을 입력하면 에러)
print(dic1.get('이름')) # 출력값 : 홍길동
print(dic1.get('학번')) # 출력값 : none // 없는 키값을 출력하려고 해도 에러는 안 남

# 추가, 수정 , 삭제 방법
dic1['math'] = 90   # 딕셔너리 추가 :: 없는 키에 값을 입력하면 추가가 됨
dic1['kor'] = 50   # 딕셔너리 값수정 :: 있는 키에 값을 입력하면 수정이 됨
del(dic1['eng'])   # 딕셔너리 값삭제 :: 삭제됨

# 평균이라는 값이 없을 때만 입력해서 넣어라
if '평균' not in dic1:
  dic1['평균'] = 99.0




print(dic1)
a_list = [1,'홍길동',100,100,100,300,100.0,1]
# a_list = [1,2,3,'홍길동']
# print(a_list[0])