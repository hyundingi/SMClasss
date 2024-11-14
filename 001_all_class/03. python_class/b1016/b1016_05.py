# 파일 자체 복사
f = open('C:/workspace/SMClasss/b1016/img/1.jpg','rb')
fData = f.read()
f.close()
print('파일 읽기 성공!')

ff = open('C:/workspace/SMClasss/b1016/img/2.jpg','wb')
len = ff.write(fData)
print(f'파일크기 : {len} 바이트')
ff.close()

# 파일(바이너리파일) 자체 읽어오기 (안에 있는 내용을 읽어오는 게 아님)
# f = open('C:/workspace/SMClasss/b1016/img/1.jpg','rb')
# fData = f.read()
# f.close()

# print('파일 읽기 성공!')



# 문서파일 읽기r, 쓰기w, 이어쓰기a, 문서 내용을 복사(아래)
# txt 파일의 내용을 복사
# f = open('b1016/students.txt','r',encoding='utf-8')
# ff = open('b1016/students2.txt','w',encoding='utf-8')

# while True:
#   line = f.readline()
#   if not line: 
#     break
#   ff.write(line)
#   print(line.strip())
# f.close()
# ff.close()
