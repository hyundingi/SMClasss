class Students:

  count = 0       
  students = []    # 클래스 리스트

  # 클래스 함수
  @classmethod    
  def stu_print(cls):
    print('-'*60)
    for s in cls.students:
      print(str(s))

  def __init__(self,name,kor,eng,math):
    Students.count += 1
    self.no = Students.count
    self.name = name     # 클래스 내에 name 이라는 변수를 만들어서(self.name) name 값을 넣어달라는 뜻
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor+eng+math
    self.avg = round((kor+eng+math)/3,2)
    self.rank = 0
    # 클래스 리스트에 추가
    Students.students.append(self)

# 객체를 문자열로 리턴 (리턴함수) 항상 문자열이 되어야함
  def __str__(self):
    return f'{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}'

  def print(self):
    return {'no':self.no,'name':self.name,'kor':self.kor,'eng':self.eng,'math':self.math,'total':self.total,'avg':self.avg, 'rank':self.rank}


# -------------- 프로그램 시작 --------------------------
# 클래스 - 변수, 함수의 집합체
s_t =  ["no","name","kor","eng","math","total","avg","rank"]
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수


while True:
  print('[학생성적 프로그램]')
  print('1. 학생성적입력')
  print('2. 학생성적출력')
  print('3. 홍길동, 유관순 비교')
  choice = int(input('원하는 번호를 입력하세요. >> '))

  if choice == 1:
    print('[학생성적입력]')
    name = input('이름을 입력하세요. >> ')
    score = []
    for i in range(2,5):
      score.append(int(input(f'{s_title[i]}')))
    # students 딕셔너리 타입으로 변경해서 입력
    s1 = Students(name,*score) # 전개 연산자 사용 s1 = Students(name,score[0],score[1],score[2]) 와 같은 의미
    #students.append(s1)  # class를 저장
    for s in Students.students:
      print(s)

  elif choice == 2:
    print('[학생성적출력]')
    print(*s_title, sep='\t')
    Students.stu_print() #클래스 변수 - 클래스명.함수명

  elif choice == 3:
    s1 = Students('홍길동',100,55,66)
    s2 = Students('유관순',55,77,79)







#print(s1.print())
#students.append(s1.print())
# print(s1.name)
# print('s1.count : ',s1.count)
# print('s1.no : ',s1.no)
s2 = Students('유관순',90,90,99)
# print(s2.print())
# students.append(s2.print())
# print(s2.name)
# print('s1.count : ',s2.count)
# print('s2.no : ',s2.no)
# print('s1.count : ',s1.count)
# print('s1.no : ',s1.no)

print(s1)   # 원래는 s1을 찍으면 주소값이 나왔는데 __str__ 로 정의된 형태가 출력됨
print(students)