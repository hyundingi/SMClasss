# 구구단 입력한 단까지 출력하시오
# 3 > 123단 출력

# a = int(input("숫자입력 : "))
# for b in range(1,a+1):
#   print(f"[{b}]단")
#   for c in range(1,9+1):
#     print(f"{b} x {c} = {b*c}")
#   print("-"*10)


# 000 / 001 ... / 999 로 출력

## 1번
# for a in range(0,9+1):
#   for b in range(0,9+1):
#     for c in range(0,9+1):
#       print(a,b,c)

## 2번
# for i in range(1000):
#   if i< 10:
#     print(f"00{i}")
#   elif i<100:
#     print(f"0{i}")
#   else:
#     print(i)

## 3번
# for i in range(1000):
#   print(f"{i:03d}")

# for문을 출력
for k in range(1,10):
  print(f"[ {k} 단 ]", end="\t")
print()
for i in range(2,10):
  for j in range(1, 10):
   print(f"{j} x {i} = {i*j}", end="\t")
  print()