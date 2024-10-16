import os

# mkdir : 현재 폴더만 생성
# makedirs : 현재폴더, 하위폴더까지 생성해줌
# os.path.exists() : 현재 폴더가 존재하는 지 확인

if not os.path.exists('c:/ccc'): # c드라이브에 bbb라는 폴더가 없다면,
  os.makedirs('c:/ccc')

f = open('c:/ccc/c.txt','w',encoding='utf=8')
f.write('안녕하세요')
f.close()