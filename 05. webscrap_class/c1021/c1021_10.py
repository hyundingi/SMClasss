import requests
from bs4 import BeautifulSoup

url = 'https://www.melon.com/index.htm'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)

soup = BeautifulSoup(res.text, 'lxml')

Data = soup.find('div',{'class':'hot_issue'}).find('li',{'class':'issue_list04'}).find_all('dl')


for idx, song in enumerate(Data):
  print('제목 : ', Data[idx].find('span',{'class':'title'}).text)
  print('가수 : ', Data[idx].find('span',{'class':'ellipsis'}).text)
  print('이미지 : ', Data[idx].find('img')['src'])
  with open (f'c1021/m{idx+1}.jpg','wb') as f:
    re_img = requests.get(Data[idx].find('img')['src'])
    f.write(re_img.content)
# print('이미지 : ', Data.find('img'))
