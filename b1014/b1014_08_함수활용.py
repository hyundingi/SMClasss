# 전역변수인 경우 함수내에서도 사용이 가능하고, 
#  return을 사용하지 않아도 함수 외부에서 사용이 가능함.
def calc():
  global sum # 전역변수인 경우, 함수에서 변경 시 외부에서도 같이 변경이 됨.
  sum = 100

sum = 10
calc()
print(sum)

### !! 매개 변수가 일반 변수(문자열, 숫자형, 정수형, 논리형)일 경우 
# return 하지 않으면 변수 값이 변동이 없음.
# hh = 100
# def add(hh):
#   hh = hh + 100
# add(hh)
# print(hh)

# -----------------------------
### 복합변수(변수 한개에 여러개의 값이 저장되어 있을 경우 ex. 리스트 , 딕셔너리) 
# hong = [1,2,3,4,5]

# ### !!!매우중요!!! 복합 변수를 매개 변수로 전달하면, return이 없어도 값이 변경되어 전달 됨
# def add(h):
#   for i in range(len(h)):
#     h[i] = h[i]+100

# add(hong)
# print(hong)  # 출력값 : [101, 102, 103, 104, 105]

# kim = []
# kim = hong     # 얕은 복사
# kim[0] = 100
# print(hong)



# def calc(n1,n2):
#   s1 = n1+n2
#   s2 = n1=n2
#   s3 = n1*n2
#   s4 = n1/n2
#   ss = [s1, s2, s3, s4]
#   return ss

# # s1, s2, s3, s4 = calc(10,5)
# # print(s1)
# # print(s2)
# # print(s3)
# # print(s4)
# ss = calc(10,5)
# print(ss)

# 함수 내에 선언된 변수는 외부에서 사용할 수 없음.
# def calc(v1, v2):
#   # global sum           # 전역 변수 (외부에 있는 sum의 값을 가져와서 사용할 수 있따.)
#   # sum = 0              # 지역 변수
#   for i in range(v1,v2+1):
#     sum += i
#   return sum # 내부에 있는 sum을 바깥으로 내보낼 수 있게함

# sum = 100  # 외부의 변수를 사용해서 계산을 하고 싶을 경우
# sum = calc(1,10)
# print(sum)

# print(1,2,3, sep='$', end='\t') # 가변 매개 변수, end값&sep값 : 키워드 매개 변수 (디폴트값 \n / "")
# print('안녕')

######### 키워드 매개 변수
# def calc(n1 = 10, n2=20): ## 디폴트값 10 설정
#   print(n1)
#   print(n2)

# # 값이 없으면 디폴트값이 나오고 있으면 있는 값 출력
# calc()        # 출력값 : 10 20  | 매개변수가 없으면 기본값으로 출력 됨
# calc(50)      # 출력값 : 50 20  | 키가 없으면 무조건 1번째로 전달됨
# calc(n2=100)  # 출력값 : 10 100 | 키(n2=)가 있으면 키값으로 전달이 됨

###3###### 기본 매개 변수 : 매개 변수의 개수가 동일해야함.
# def calc(n1,n2,n3):
#   print(n1+n2+n3)
# calc(1,2) # 개수 에러
# calc()    # 개수 에러


####### 가변 매개 변수 : 변수의 개수를 맞출 필요 없음
# def calc(*n):
#   print(n) 
#   print(n[0])
# calc(1,2,3) # 출력값 : (1, 2, 3) [튜플]



# num = int(input('숫자를 입력하세요. >> '))
# num2 = int(input('숫자를 입력하세요. >> '))

# 배열로 받아 계산 
# def calc(numStrr): # 배열
#   s1 = 0
#   s2 = 0
#   s3 = 1
#   s4 = 1
#   for i in range(len(numStrr)):
#     s1 += numStrr[i]
#     s2 -= numStrr[i] 
#     s3 *= numStrr[i] 
#     s4 /= numStrr[i] 
#   print(f'수의 더하기 : {s1}')
#   print(f'수의 빼기 : {s2}')
#   print(f'수의 곱하기 : {s3}')
#   print(f'수의 나누기 : {s4}')

# numStr = input('숫자를 입력하세요. (12,5,1) >> ')
# numStrr = numStr.split(',')
# numStrr = [int(i) for i in numStrr]  # 리스트 내포
# print(numStrr)
# calc(numStrr)


#### 두 수를 입력받아 함수를 활용하여 계산
# 1) 수 따로 받기
# num = int(input('숫자 1 입력 >> '))
# num2 = int(input('숫자 2 입력 >> '))

# 2) 수 같이 받기
# numStr = input('숫자를 입력하세요. (12,5,1) >> ')
# numStrr = numStr.split(',')
# # print(numStrr) # 출력값 : ['12', '5']
# num = int(numStrr[0])
# num2 = int(numStrr[1])
# num3 = int(numStrr[2])


# def calc(num,num2):
#   print(f'두 수 더하기 : {num+num2}')
#   print(f'두 수 빼기 : {num-num2}')
#   print(f'두 수 곱하기 : {num*num2}')
#   print(f'두 수 나누기 : {num/num2}')
#   print('-'*30)
# calc(num, num2)

# def calc2(num, num2, num3):
#   print(f'세 수 더하기 : {num+num2+num3}')
#   print(f'세 수 빼기 : {num-num2-num3}')
#   print(f'세 수 곱하기 : {num*num2*num3}')
#   print(f'세 수 나누기 : {num/num2/num3}')
#   print('-'*30)
# calc2(num, num2, num3)





# 함수 활용하여 계산
# def calc(num, num2):
#   print(f'두 수 더하기 : {num+num2}')
#   print(f'두 수 빼기 : {num-num2}')
#   print(f'두 수 곱하기 : {num*num2}')
#   print(f'두 수 나누기 : {num/num2}')
#   print('-'*30)

# num = [10, 20, 30]
# num2 = [5, 7, 3]
# for i in range(len(num)):
#   calc(num[i],num2[i])




# # for 문 활용하여 계산
# num = [10, 20, 30]
# num2 = [5, 7, 3]

# for i in range(len(num)):
#   print(f'두 수 더하기 : {num[i]+num2[i]}')
#   print(f'두 수 빼기 : {num[i]-num2[i]}')
#   print(f'두 수 곱하기 : {num[i]*num2[i]}')
#   print(f'두 수 나누기 : {num[i]/num2[i]}')
#   print('-'*30)

