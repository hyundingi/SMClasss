import os
import requests
from bs4 import BeautifulSoup

  

url = 'https://www.melon.com/chart/index.htm'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status() 

soup = BeautifulSoup(res.text, 'lxml')
# print(soup.prettify())

# 순위, 사진 링크 주소, 노래 제목

# 1. 기준점
Data = soup.select_one('#frm > div > table')
lists = Data.select('tr')

# 상단 타이틀
title = []
tits = lists[0].select('th')
for tit in tits:
  title.append(tit.text.strip())
# print(title)

# 노래 차트 1-100위 리스트
for i in range(1,101):
  # 폴더가 존재하지 않으면
  if not os.path.exists('c1022/melon'):
    os.makedirs('c1022/melon')
  lis = lists[i].select('td')
  singers = lis[5].select('div.rank02 > a')
  if len(singers) <= 1:
    print(f'{lis[1].select_one('span').text}위 {lis[5].select_one('a').text} / {singers[0].text}')
  else:
    print(f'{lis[1].select_one('span').text}위 {lis[5].select_one('a').text} / {singers[0].text},{singers[1].text}')
  print('앨범 이미지 : ', lis[3].select_one('img')['src'])

  with open(f'c1022/img/{i}위.jpg','wb') as f:
    re_img = requests.get(lis[3].select_one('img')['src'])
    f.write(re_img.content)






# song_Data = soup.select('tr#lst50')
# print(song_Data)
# song_img = song_Data.select('a.image_typeAll')
# song_title = song_Data.select('div.wrap_song_info')
# print(song_title.select_one('div.rank02 > a').text)  # 가수
# print(song_title.select_one('a').text)    # 노래 제목
# print(song_img.select_one('img')['src'])  # 앨범 이미지

#for idx, song in enumerate(song_Data):
  # print('이미지 주소 : ', song[idx].select_one('a.image_typeAll').select_one('img')['src'])
  # print('순위 : ', i-4)
  # print('제목 : ', song_title[i-5].select_one('a').text)
  # print('가수 : ', )