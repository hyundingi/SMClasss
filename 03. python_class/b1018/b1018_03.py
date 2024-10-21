# 클래스 생성
class Car:
  
  def __init__(self, color,tire,gear,speed):
    self.color = color
    self.tire = tire
    self.gear = gear
    self._speed = speed

  color = '흰색'
  speed = 0

  def upSpeed(self,value):
    if value > 0:
      self._speed += value
    else:
      raise '값 혹은 함수 다시 확인'

  def downSpeed(self,value):
    self._speed -= value

# 클래스 선언을 꼭 해야함
c1 = Car('흰색',4,'auto',0)
c1.color = '파랑'
print(c1.color)
c1._speed = '300'
print(c1._speed)
# c1 = Car()
# print(c1.color)

# c2 = Car()
# c2.color = '빨강'
# print(c2.color)
# 리스트, 딕셔너리 변수 직접 값을 할당하는 방식


# 1) speed 변수에 직접 값을 할당해서 출력하는 방법
# c1.speed = 100
# print(c1.speed)

# 2) 함수를 활용해서 값을 할당
# c1.upSpeed(100)
# print(c1.speed)
