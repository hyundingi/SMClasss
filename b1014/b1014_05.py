subName = ['국어', '영어', '수학']
score = {'국어':100, '영어':95, '수학':80}
print(score['국어'])
print(score[subName[0]])

# 출력값 : 
# 국어 : 100
# 영어 : 95
# 수학 : 80

# 1번 방법
for i in subName:
  print(f'{i} : {score[i]}')

# 2번 방법
for k,v in score.items():
  print(k, ':', v)

# # 구구단 출력
# def calc(n):
#   for i in range(2, n+1):
#     print(f'[{i}단]')
#     for j in range(1, 9+1):
#       print('{} * {} = {}'.format(i, j, i*j))

# nArr = [9,5,7]
# #  2-9단, 2-5단, 2-7단
# for i in nArr:
#   calc(i)
#   print('-'*50)



# 2-5단
# for i in range(2,5+1):
#   print(f'[{i}단]')
#   for j in range(1,9+1):
#     print(f'{i} * {j} = {i*j}')
# calc(2,5)

# # 3-9단
# calc(3,9)

# # 5-8단
# calc(5,8)