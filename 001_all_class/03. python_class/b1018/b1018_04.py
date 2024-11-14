# 절차적인 형태의 프로그램 구현
# 반지름을 입력받아, 원의 둘레와 넓이를 출력하시오.

# r = int(input('반지름을 입력하세요.'))
# print('원의 둘레 :', r*2*3.14)
# print('원의 넓이 :', r**2*3.14)

# 클래스 생성
class Circle:
  def __init__(self, length):
    self.length = length      # 변수에 직접적으로 접근 제한 _

  def get_area(self):
    return self.length**2*3.14
  def get_cir(self):
    return self.length*2*3.14

    
# 클래스 선언
c1 = Circle(int(input('반지름을 입력하세요.')))
print('넓이 : ',c1.get_area())
print('둘레 : ',c1.get_cir())

c2 = Circle(int(input('반지름을 입력하세요.')))
print('넓이 : ',c2.get_area())
print('둘레 : ',c2.get_cir())