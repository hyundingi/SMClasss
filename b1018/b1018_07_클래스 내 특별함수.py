# a = [1,2,3]
# print(*a)   # 전개연산자

# s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
# print(*s_title, sep='\t')
# print(s_title)

class Students:
  count = 0       
  
  def __init__(self,name,kor,eng,math):
    Students.count += 1
    self.no = Students.count
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor+eng+math
    self.avg = round((kor+eng+math)/3,2)
    self.rank = 0

  # == 를 썻을 때 : 호출되는 함수
  def __eq__(self, value):    # self: 현재 자신의 객체 / value: 비교할 다른 객체
    return self.total == value.total
  def __ne__(self, value):    # self: 현재 자신의 객체 / value: 비교할 다른 객체
    return self.total != value.total
  def __gt__(self, value):    # self: 현재 자신의 객체 / value: 비교할 다른 객체
    return self.total > value.total
  def __ge__(self, value):    # self: 현재 자신의 객체 / value: 비교할 다른 객체
    return self.total >= value.total
  def __lt__(self, value):    # self: 현재 자신의 객체 / value: 비교할 다른 객체
    return self.total < value.total
  def __le__(self, value):    # self: 현재 자신의 객체 / value: 비교할 다른 객체
    return self.total <= value.total

s1 = Students('홍길동',100,100,100)
s2 = Students('유관순',100,100,100)

if (300>290):
  print('숫자 비교 참입니다.')
else:
  print('숫자 비교 거짓입니다.')

if (s1 == s2):
  print('개체 비교 참입니다.')
else:
  print('개체 비교 거짓입니다.')