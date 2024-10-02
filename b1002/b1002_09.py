fruit = '사과,배,딸기,포도,복숭아,배,사과,배,딸기'
# print(fruit.find("딸기", 0)) # 딸기를 0번 부터 찾기
# print(fruit.find("딸기", fruit.find("딸기", 0)+1))

fruits = fruit.split(",")
print(fruits)
print("전체 개수 : ", len(fruits))

# 리스트 인 경우 검색해서 해당되는 index를 출력하시오.
# 배에 해당되는 index 번호를 출력


# for i in range(fruit.count(search)):
#   print(fruit.find(search, 0))
#   print(fruit.find(search, 0), fruit.find(search, 0)+1)

search = input("과일 이름 입력 : ")
for idx, f in enumerate(fruits):
  if f == search:
    print("해당 위치 : ", idx)