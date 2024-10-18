class Circle:
  def __init__(self,length):
    self.__length = length    # 내부 클래스만 변수에 접근해서 수정이 가능함. / 
    pass
# 원의 넓이와 길이 함수 
  def get_area(self):
    return self.__length**2*3.14
  def get_cir(self):
    return self.__length*2*3.14
  
  def __str__(self):
    c_str = '원의 길이 : {}, 원의 넓이 : {}, 원의 둘레 : {:.2f}'.format(self.__length,self.get_area(),self.get_cir())
    return c_str
  
  def get_length(self):
    return self.__length
  def set_length(self, length):
    self.__length = length

# 클래스 선언
# _, 내부적으로 캡슐화 하겠다고 선언함.
# __, 다른 변수로 할당

c1 = Circle(10)                                # 선언 - 값을 입력
# print('c1의 길이 : ',c1.get_length())          # getter 값 출력
# c1.set_length(200)                             # setter 값을 입력
# print('c1의 길이 변경: ',c1.get_length())      # getter 값 출력
# c1.__length = 100                                # 변수 직접입력
# print('직접변경 : ', c1.__length)                 # 변수 직접출력
# print('get 읽어온 length : ', c1.get_length())   # getter 값 출력

print(c1)