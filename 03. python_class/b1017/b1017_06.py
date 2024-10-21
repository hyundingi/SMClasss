a = ['20', 'vciccettij', '51', '100', '99', '250', '83.33333333', '1']
b = ['20', '51', '100', '99', '250', '83.33333333', '1']
t_title = ['no','name','kor','eng','math','total','avg','rank']
students = []


def f_float(value):
  if value.isdigit():            # 정수인지, 실수, 문자열인지
    return int(value)
  else:
    try:
      return float(value)        # 실수일때 실수로 변환
    except:
      return value               # 문자열일때 그대로 리턴

# 문자열, 정수, 실수로 구성
c = []
for idx, value in enumerate(a):
  c.append(f_float(value))

# students 리스트에 딕셔너리로 저장
students.append(dict(zip(t_title,c)))
print(students)

# 숫자로만 구성 - 정수, 실수
# for idx, value in enumerate(b):
#   if value.isdigit():   # isdigit() - 정수 True/ 실수 False
#     print(f'{idx}번째 {type(int(value))}')
#   else:
#     print(f'{idx}번째 {type(float(value))}')



# # try-except 구문을 사용해서 정수, 실수 구분.
# def t_float(n):
#   try:
#     int(n)
#     return True
#   except:
#     return False
  
# # 문자열인지 아닌지 구분
# for idx, i in enumerate(a):
#   if i.isdigit():
#     print(f'{idx}번째 {i}는 숫자입니다.')
#   else:
#     print(f'{idx}번째 {i}는 문자입니다.')

# 정수로 변경
# for i in b:
#   if t_float(i):
#     i = int(i)
#   else:
#     i = float(i)
#   c.append(i)
# print(c)


# b의 리스트 float으로 변경
# b의 형태가 모두 숫자이기 때문에 float으로는 전부 변경 가능함.
# for i in b:
#   c.append(float(i))
# print(c)