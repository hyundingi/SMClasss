# Student 클래스 생성 후
# 데이터를 직접 입력받아 클래스 선언 후 저장
# 번호 - 자동 부여 , 이름, 국어 영어 수학 합계 평균 등수
# 클래스 전체 출력
# 클래스 수정

class Student:
  count = 0
  students = []

  def __init__(self,name,kor,eng,math):
    Student.count += 1
    self.no = Student.count
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor+eng+math
    self.avg = round((kor+eng+math)/3,2)
    self.rank = 0
    Student.students.append(self)

  def __str__(self):
    return f'{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}\t'
  

s_t =  ["no","name","kor","eng","math","total","avg","rank"]
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']

while True:
  print('[학생성적프로그램]')
  print('1. 학생성적입력')
  print('2. 학생성적출력')
  print('3. 학생성적수정')
  choice = input('원하는 번호 입력 >> ')

  if choice == '0':
    break
  elif choice == '1':
    while True:
      print()
      print('[학생성적입력]')
      name = input('이름을 입력하세요. >> ')
      if name == '0':
        break
      
      score = []
      for s in range(2,5):
        score.append(int(input(f'{s_title[s]} 점수를 입력하세요. >> ')))
      s1 = Student(name, *score)

  elif choice == '2':
    print('[학생성적출력]')
    for t in range(len(s_title)):
      print(s_title[t], end='\t')
    print()
    print('-'*60)
    for s in Student.students:
      print(s)

  elif choice == '3':
    while True:
      print('[학생성적수정]')
      name = input('수정할 학생 이름 입력 >> ')
      if name == '0':
        break
      for s in Student.students:
        if s.name == name:
          print(f'{name}찾았습니다.')
          print('[수정항목선택]')
          print('1. 국어점수')
          print('2. 영어점수')
          print('3. 수학점수')
          choice = int(input('수정 항목 번호 입력 >> '))
          if choice == 1:
            print(f'현재 국어 점수 : {s.kor}')
            s.kor = int(input('수정할 점수 : '))
            print('변경되었습니다.')
          elif choice == 2:
            print(f'현재 영어 점수 : {s.eng}')
            s.eng = int(input('수정할 점수 : '))
            print('변경되었습니다.')
          elif choice == 3:
            print(f'현재 영어 점수 : {s.math}')
            s.math = int(input('수정할 점수 : '))
            print('변경되었습니다.')
          s.total = s.kor+s.eng+s.math
          s.avg = round(s.total/3,2)

          
      else:
        print('없습니다.')
