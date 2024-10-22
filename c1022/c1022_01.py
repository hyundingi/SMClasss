import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status()  # 에러시 종료

# print(res.text)     # 타입 : str

# html, css 파싱이 되어서 예브게 출력
# print(soup.prettify())

# 태그를 활용한 검색방법
# find , find_all <> select_one, select

soup = BeautifulSoup(res.text, 'lxml') 
# print(soup.find('h2', {'class':'rankingnews_tit'}))
# print(soup.select_one('h2.rankingnews_tit'))

data = soup.select_one('div.rankingnews_box_wrap')
title = data.select("div.rankingnews_box")
news_list = title.select('ul.lanking_list>li')
print(news_list)
# for i, n in enumerate(title):
#   print('언론사 : ', n[i].select_one('strong.rankingnews_name').text)
#   for i, t in enumerate(news_list):
#     print('뉴스 : ', t[i].select_one('a').text)
