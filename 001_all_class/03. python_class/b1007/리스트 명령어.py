###### !!!!  리스트 함수
# a_list = [1,2,3,4,5,60,3,70,3]
# print(len(a_list))     # 리스트의 개수 알려주는 함수 
# print(a_list.count(3)) # 입력된 값의 존재 개수 확인 / 출력값 : 3 (리스트에 3이 3개 있다는 뜻)

# 추가 함수
# a_list.insert(0, 100)  # 0번째 자리에 100 추가
# a_list.append(200)     # 리스트 제일 뒤에 값 추가

# 삭제 함수
# a_list.pop(2)      # index 위치의 해당값 삭제
# a_list.clear()     # 전체 삭제
# a_list.remove(5)   # 리스트의 값 중 원하는 값을 찾아 삭제
# del a_list[0]      # 0번째 삭제 / 출력값 : [2,3,4,5]



### 리스트 삭제
# a_list = [1,2,3,4,5]
# a_list = None    # 전체 삭제
# a_list = []      # 전체 삭제
# a_list.clear()   # 전체 삭제
# a_list[1:3] = [] # 1번째 2번째 값 삭제
# a_list.remove(5) # 리스트의 값 중 원하는 값을 찾아 삭제
# print(a_list) 

# 리스트 삭제 - del 명령어 사용
# del(a_list) # a_list 자체를 삭제
# del a_list[0] # 0번째 삭제 / 출력값 : [2,3,4,5]
# print(a_list) 

### 리스트 수정 방법
# a_list = [1,2,3,4,5,6,7]
# a_list[3] = 50           # 1개 변경
# a_list[1:3] = [20,30]    # 2개 변경
# a_list[4] = [10,20]      # 리스트 안에 리스트로 변경
# print(a_list)



#### 리스트 출력 방법
# a_list = [1,2,3,4,5]
# b_list = [50, 100]
# a_list[0:3] # 출력값 : [1, 2, 3]
# a_list[2:4] # 출력값 : [3, 4]
# a_list[:3]  # 출력값 : [1, 2, 3]
# a_list[3:]  # 출력값 : [4, 5]
# print(a_list+b_list)  # 출력값 : [1, 2, 3, 4, 5, 50, 100]
# print(b_list * 3)     # 출력값 : [50, 100, 50, 100, 50, 100] (3번 반복해서 출력)
# print(a_list[::2])    # 출력값 : [1, 3, 5] 
# print(a_list[::-2])   # 출력값 : [5, 3, 1]
# print(a_list[::-1])   # 출력값 : [5, 4, 3, 2, 1]



##### 얕은 복사 - 주소값이 같음, 깊은 복사 - 주소값이 다름
# a_list = [1,2,3]
# b_list = a_list # 얕은 복사 
# a_list[0] = 100 # a리스트의 값을 변경하면 b리스트의 값도 변경됨
# print(a_list)  # 출력값 : [100, 2, 3]
# print(b_list)  # 출력값 : [100, 2, 3]

# a_list = [1,2,3,4,5]
# b_list = a_list[::-1] # 깊은 복사(리스트를 역순으로 저장)
# b_list = a_list[:]     # 깊은 복사
# a_list[0] = 100     # a리스트의 값을 변경해도 b리스트의 값은 변경 안 됨
# print(a_list)       # 출력값 : [100, 2, 3, 4, 5]
# print(b_list)       # 출력값 : [5, 2, 3, 4, 5]


# 역순으로 값 출력 - 1번
# for i in range(1, len(a_list)+1):
#   print(a_list[-i])

# 역순으로 값 출력 - 2번
# for i in range(len(a_list)):
#   print(a_list[-(i+1)])



# # 문자열, 숫자-정수, 숫자=실수, 논리형
# a_list = [1,2,3.0,'안녕',True,False]
# print(a_list[0])
# print(a_list[3])
# print(a_list[-1])



# a_list = []
# # 1- 100 들어가있는 리스트 출력
# total = 0
# for i in range(1,100+1):
#   a_list.append(i)
#   total += i
# print(a_list)
# print("합계 : ", total)



# a_list = []
# total = 0

# for i in range(10):
#   j = int(input(f"{i+1}번째 숫자를 입력하세요. >> "))
#   a_list.append(j)
#   total += j

# print("합계 : ", total)


# a_list 에 범위가 지정되어있는 경우
# for idx, a in enumerate(a_list):
#   a = int(input(f"{idx+1}번째 숫자를 입력하세요. "))
#   total += a

# print("합계 : ", total)

# a,b,c,d,e,f,g = 0,0,0,0,0,0,0
# total = 0

# # a,b,c,d,e 의 변수에 숫자를 입력받아 합계 출력 
# a = int(input("숫자1를 입력하세요. "))
# b = int(input("숫자2를 입력하세요. "))
# c = int(input("숫자3를 입력하세요. "))
# d = int(input("숫자4를 입력하세요. "))
# e = int(input("숫자5를 입력하세요. "))
# f = int(input("숫자6를 입력하세요. "))
# g = int(input("숫자7를 입력하세요. "))

# total = a+b+c+d+e+f+g
# print("합계 : ", total)