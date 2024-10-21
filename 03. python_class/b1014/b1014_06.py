import random
fruit = {'바나나':'banana', '오렌지':'orange', '체리':'cherry', '파인애플':'pineapple', '코코넛':'coconut'}
# fName = ['바나나', '오렌지', '체리', '파인애플', '코코넛']

fName = list(fruit.keys()) # fName = ['바나나', '오렌지', '체리', '파인애플', '코코넛']
print(list(fruit.keys()))


## fName 랜덤으로 영문 퀴즈 진행됨
# re_fName = random.sample(fName, 5)

# for i in re_fName:
#   print(f'{i}의 영문을 입력하세요.')
#   search = input('>> ')
#   if fruit[i] == search:
#     print('정답입니다.', fruit[i], search)
#   else:
#     print('오답입니다.', fruit[i], search)






## fName 순서대로 영문 퀴즈 진행됨
# count = 0
# print('[영단어 맞추기]')
# for key in fruit.keys():
#   print(f'{key}의 영문을 입력하세요.')
#   search = input('>> ')
#   if fruit[key] == search:
#     print('정답입니다.', fruit[key], search)
#     count += 1
#   else:
#     print('오답입니다.')
# print(f'당신의 점수 : {count}')






# 한글로 입력하면 영문이 나오도록
# while True:
#   search = input('과일 입력 >> ')
#   if search in fruit:
#     print('영문으로 : ', fruit[search])
#   else:
#     print('찾는 단어가 없습니다.')
  