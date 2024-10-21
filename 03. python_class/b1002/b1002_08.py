# 리스트
# in - 데이터가 있는지 확인
# count - 데이터 개수
# find - 데이터가 있는 위치, 없으면 -1  find(검색어, 시작위치, 끝위치)
# index - 데이터가 있는 위치, 없으면 에러
# range - b1002_05_for 파일 참고 () 에 들어간 수만큼 반복
# enumerate :: index 번호를 가져올 수 있음


fruit = '사과,배,딸기,포도,배,사과, 배, 딸기, 복숭아'
# 배가 있는 위치를 모두 출력하시오
search = input('과일 이름 임력 : ')
print("모든 글자 : ", fruit)
idx = 0
if fruit.count(search)>0:
  print(f'{search} 글자가 있습니다.')
  for i in range(fruit.count(search)):
      print(f'{search} 글자가 있는 위치 :', fruit.find(search,idx))
      idx = fruit.find(search,idx)+1
else:
  print(f'{search}라는 글자는 없습니다.')

    



# fruit = ['사과', '배', '딸기', '포도', '배']

# if '배' in fruit:  # 1번의 비교로 있는 지 확인
#   print("배가 있어요")
# else:
#   print("배가 없어요")


# fruit = "사과, 배, 딸기, 포도"
# if '배' in fruit:
#   print("배라는 글자가 있어요")
# else:
#   print("배라는 글자가 없어요")


# fruit = ['사과', '배', '딸기', '포도', '배']
# # 글을 입력받아 입력한 과일이 있으면 있어요

# f = input("과일 입력 : ")
# if f in fruit:
#   print("있어요")
# else:
#   print("없어요")


# .count : 리스트에서 개수 확인 
# fruit = ['사과', '배', '딸기', '포도', '배', '사과', '배', '딸기', '복숭아']
# print(fruit.count('배'))
# print(fruit.count('사과'))

# .count : 문자열에서 개수 확인
# fruit = '사과,배,딸기,포도,배,사과, 배, 딸기, 복숭아'
# # print(fruit.count('사과'))


# # 과일 이름을 입력받아 있으면 있다, 개수 
# fname = input("과일 이름 입력 : ")

# if fname in fruit:
#   print(fname, '는', fruit.count(fname), '개 있습니다.')
# else:
#   print(fname, '은 없습니다.')
#   print(fruit.index(fname)) # 배가 있는 위치의 index (데이터가 없으면 에러가 뜸)
#   print(fruit.find(fname)) # index 위치 찾기 (데이터가 없으면 -1이 뜸 / 에러는 안 남)