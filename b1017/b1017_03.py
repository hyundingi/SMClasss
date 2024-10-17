# --------- 예외 처리 try - except 구문을 사용해서 처리
# print('프로그램 시작')
# # print('프로그램 시작)     # 구문에러 : 아예 실행이 안 됨
# # print(list_a)              # 런타임 오류 : 프로그램 실행 중에 오류 

# try:                            
#   print(list_a)
# except:
#   print('에러 발생')

# print('프로그램 종료')


# n_str = input('반지름을 입력하세요. >> ')
# try:
#   num = int(n_str)
#   # 원 넓이, 원 둘레
#   print('원 넓이 : ',num*num*3.14)
#   print('원 둘레 : ',num*2*3.14)
# except Exception as e :                       # 어떤 에러가 났는지 보여줌
#   print('정수가 아님. 에러',e)



# 숫자에 **2를 하는 프로그램 구현
# list_a = [1,2,3,4,5,'홍길동']
# list_b = []

# try:
#   for a in list_a:
#     list_b.append(a**2)
# except Exception as e:
#    print(e)
# print(list_b)


# try 구문에 에러가 발생해야 except 실행시킴
# 에러 없음 : try > else > finally > 구문 밖 
# 에러 잇음 : try (중단)> except > finally > 구문 밖
print('1')
try:
  print('2')
  #print(3/0)
  print('3')
  print('4')
except:
  print('5')
  print('6')
else:
  print('7')
  print('8')
finally:
  print('끝')
print('8')
print('8')

f = open('b1017/a.txt','w',encoding='utf-8')
try:
  f.write('안녕하세요\n')
  f.write('안녕\n')
  f.write('하세요\n')
  f.write({'a':1})
  f.write('안녕하세요')
except Exception as e:
  print(e)
finally:
  f.close()