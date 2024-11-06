import requests
from bs4 import BeautifulSoup

url = 'https://m.search.daum.net/search?w=tot&q=%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}
res = requests.get(url, headers=headers)
res.raise_for_status()

# soup 변환
soup = BeautifulSoup(res.text, 'lxml')
with open('c1021/html/screen.html','w',encoding='utf-8') as f:
  f.write(soup.prettify())

# 1-10 제목 예매율

# test_title = soup.find('div',{'id':'morColl'}).find('c-title',{'slot':'title'})
# title = soup.find('div',{'id':'morColl'}).find_all('c-title',{'slot':'title'})
# cont = soup.find('div',{'id':'morColl'}).find_all('c-title',{'slot':'contents'})

# print(soup.find('div',{'class':'item-title'}).find('strong',{'class':'tit-g clamp-g'}))
data = soup.find('c-flicking',{'id':'mor_history_id_0'})
screens = data.find_all('c-doc')

for idx, d in enumerate(screens):
  print('순위 : ', screens[idx].find('c-badge-text').next)
  print('영화명 : ', screens[idx].find('c-title').next)
  print('예매율 : ', screens[idx].find('c-contents-desc').next)
  print('날짜 : ', screens[idx].find('c-contents-desc-sub').next)

# for i, t in enumerate(title):
#   print(f'{i} : {t.text} ')