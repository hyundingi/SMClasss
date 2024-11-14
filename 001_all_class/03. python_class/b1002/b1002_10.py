fruit = []

# 입력된 과일이름을 리스트에 추가하시오.
# strip() 앞쪽 여백, 뒤쪽 여백 제거 trim '사과 ' > '사과' 
# '사 과' > '사 과' 의 경우 replace(" ","") :: 문자 대체 함수
while True:
  # name = input('과일 이름 입력 : ').strip()
  name = input('과일 이름 입력 : ').replace(" ","")
  if name == 'x':
    break

  if name in fruit:
    print("이미 등록되어 있는 과일 입니다.")
    print(fruit)
  else:
    fruit.append(name)
    print(fruit)







# while True:
#   search = input('과일이름을 입력하세요(종료: x)')
#   if(search == 'x'):
#     break

# while True:
#   break # 반복문 일때만 사용
# print("프로그램 종료")

# a = 0
# while True: # 무한대로 실행
#   print(a)
#   a += 1

# while (a<10):
#   a += 1
#   print(a)

# print("프로그램 종료")