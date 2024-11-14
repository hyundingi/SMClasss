# 객체 선언 -----------------------------------------------------------
  # 참조변수명 = 클래스명()  ex ) s1 = Students()
  # 변수 3종류 -----------------------------------------------------------
  # 1) 인스턴스 변수(self. ~ no, name 등)
  # - 객체선언 할 때 만들어짐. 각각의 객체마다 변수가 생성됨
  # - 사용법 : 참조변수.변수명
  # 2) 클래스 변수
  # - 객체가 선언되지 않아도 만들어짐. 객체를 공통으로 사용
  # - 사용법 : 클래스명.변수명, 
  # 3) 지역 변수
  # - 함수 내에 선언된 변수. 함수가 종류가 되면 사라짐

  # 함수 2종류 ----------------------------------------------------------
  # 1) 인스턴스 함수 
  # - 객체선언 할 때 만들어짐. 각각의 객체마다 함수가 생성됨
  # - 사용법 : 참조변수명.함수명
  # 2) 클래스 함수
  # - @classmethod 클래스 함수 표시
  # - 객체가 선언되지 않아도 만들어짐. 모든 객체를 공통으로 사용
  # - 사용법 : 클래스명.함수명

  # 객체 선언 한 참조변수를 출력하면 > 주소값이 출력됨.
  # - 참조변수를 출력해서 원하는 데이터를 출력하려면, __str__함수를 사용
  # - 리턴값은 문자열이어야함
  
  # 1. 생성자 정의가 없음 -- 기본생성자
  # 2 . 생성자 정의가 있음 -- 매개 변수가 있는 생성자 (__init__)

















# 1. 학생성적입력
# 이름 국어 영어 수학 > 번호 국어 영어 수학 합계 평균 등수
# 클래스 1개가 생성이 되고
# 클래스의 참조변수(__str__)를 출력
# class Student:
#   count = 0
#   students = []
#   def __init__(self, name, kor, eng, math):
#     Student.count += 1
#     self.no = Student.count +1
#     self.name = name
#     self.kor = kor
#     self.eng = eng
#     self.math = math
#     self.total = kor+eng+math
#     self.avg = round((kor+eng+math)/3,2)
#     self.rank = 0
#     Student.students.append(self)

#   def __str__(self):
#     return f'{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}\t'


# # -------------------------------
# s_t =  ["no","name","kor","eng","math","total","avg","rank"]
# s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']

# while True:
#   print('[학생성적입력]')
#   name = input('이름을 입력하세요. >> ')
#   if name == '0':
#     break
#   score = []
#   for s in range(2,5):
#     score.append(int(input(f'{s_title[s]} 점수를 입력하세요.' )))

#   s1 = Student(name,*score)
#   for s in Student.students:
#     print(s)



