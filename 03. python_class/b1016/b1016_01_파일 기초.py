# 파일 with
# close() 를 하지 않아도 됨
with open('C:/workspace/SMClasss/b1016/aa.txt','w',encoding='utf-8') as f:
  f.write('안녕하세여')

# ------- 파일 이어 쓰기 a --------------
# while True:
#   print('[메모장]')
#   data = input('저장하려는 글자를 입력하세요.')
#   f = open('C:/workspace/SMClasss/b1016/aa.txt','a',encoding='utf-8')
#   f.write(data+'\n')
#   f.close()

# ------- 파일 쓰기 w --------------
# 파일 생성 후 글자 입력 가능
# while True:
#   print('[메모장]')
#   data = input('저장하려는 글자를 입력하세요.')
#   f = open('C:/workspace/SMClasss/b1016/aa.txt','w',encoding='utf-8')
#   f.write(data)
#   f.close()

# for i in range(1,11):
#   data = f'안녕하세요 {i} \n'
#   f.write(data)
# # f.write('안녕하세요\n')
# # f.write('안녕하세요1\n')
# # f.write('안녕하세요2\n')
# f.close()


# ------- 파일 읽기 r --------------
# 위치에 파일이 없으면 에러

# 가장 바깥 폴더의 위치에서 파일을 찾음
# f = open('a.txt', 'r', encording='utf-8')

# 1. readline() : 1줄씩 읽어오기
# 절대경로를 사용
# f = open('C:/workspace/SMClasss/b1016/a.txt','r', encoding='utf8')
# while True:
#   line = f.readline()
#   if not line: break
#   print(line.strip())  # 공백 제거(한줄단위로 출력됨)
# f.close

# 2. readlines(): 리스트 타입으로 모든 줄 가져오기
# lines = f.readlines()
# print(type(lines))
# for line in lines:
#   print(line)
#   # print(line.strip())
# f.close

# 3. read()
# for line in f:
#   print(line.strip())  

# f.close()