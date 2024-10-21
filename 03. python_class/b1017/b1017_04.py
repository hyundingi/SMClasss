# try - except - else - finally
# exception 은 모든 예외의 부모격/ 예외처리에서 마지막에 위치해야함.
# as e : e변수는 예외에 대한 설명문, type(e) : 예외객체
# IndexError : 리스트 범위 밖 호출 에러
# ValueError : 입력된 값의 변환 에러
# raise : 강제 예외 발생시킴



# list1 = [52,273,32,72,100]

# try:
#   n_input = int(input('리스트 순번에 있는 값 출력 >> '))
#   print(f'{n_input}는 리스트의 {list1[n_input]}')
# except ValueError as c:
#   print('값을 잘못 입력했습니다.', type(c))
# except IndexError as e:
#   print('번호가 범위를 벗어났습니다.', type(e))
# except Exception as e:
#   print('모든 예외처리의 부모')



print('프로그램을 시작합니다.')
print('1')
print('2')
try:
  print('3')
  print('4')
  raise NotImplementedError('프로그램을 구현해야함.')  # 강제 에러
  print('5')
except Exception as e:
  print(e)
  print('6')
  print('7')
finally:
  print('8')
  print('9')
print('10')
print('프로그램을 종료합니다.')
