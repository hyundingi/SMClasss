title = ['e_id', 'e_name','salary']
aa = [
  (196, 'Alana Walsh', 3100.0),
  (125, 'Julia Nayer', 3200.0),
  (180, 'Winston Taylor', 3200.0),
  (194, 'Samuel McCain', 3200.0),
  (138, 'Stephen Stiles', 3200.0)
]

a_list = []


for a in aa:
  a = dict(zip(title,a))
  a_list.append(a)
print(a_list)



# select * from employees where emp_name like '%a%';
# name = '홍길동'
# a = '안녕하세요. 이름은 %s 입니다.'%name
# print(a)

# # format 함수 / 문자 f 함수 / 문자변수
# print('hello. my name is {}'.format(name))
# print(f'hello. my name is {name}')
# print('hello. my name is %s'%name)


# a = 1
# b = 2

# a_list = [a,b]
# print(a_list)
# print(type(a_list))

# a_tuple = (a,b)
# print(type(a_tuple))

# # b_tuple (a) = type: int // 
# # 괄호 안에 값이 하나일 때는 두ㅣ에 쉼표를 붙여줘야 튜플이 됨
# b_tuple = (a,)
# print(type(b_tuple))
