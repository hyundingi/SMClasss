import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status

soup = BeautifulSoup(res.text,'lxml')

# 찾기 ------------------------------------------------------------------------------------------------------------------------------------
print(soup.div.li)       # 제일 먼저 찾아지는 것을 출력
# print(soup.find('div'))  # 특정 위치의 태그를 출력
print(soup.div['id'])

# find() -- 한개 검색 // 특정한 위치의 태그와 속성을 가지고 찾을 수 있음
print(soup.find('h2',{'class':'rankingnews_tit'}).text)   # h2 태그 중 class 가 rankingnews_tit 인 것의 텍스트만 가져옴

# find_all() -- 여러개 검색
# print(soup.find_all('div'))                              # 모든 div 찾기
print(type(soup.find_all('div')))                              # 타입 : <class 'bs4.element.ResultSet'> // ResultSet - 객체의 리스트
print(len(soup.find_all('div')))                              # 모든 div 의 길이
# print(soup.find_all('div',{'class':'rankingnews_box'}))    # 모든 div 중에 class가 rankingnews_box 인 것을 모두 찾음
rankingnews_wrap = soup.find('div',{'class':'rankingnews_box_wrap'})
# print(rankingnews_wrap)
# rankingnews_boxs = rankingnews_wrap.find_all('div',{'class':'rankingnews_box'})
rankingnews_boxs = rankingnews_wrap.find('div',{'class':'rankingnews_box'})
print(1, '='*20)
print(rankingnews_boxs)
print(2, '='*20)
# next 검색태그 다음 뒤에 오는 태그를 찾아줌
# next_sibling 검색태그의 형제관계의 다음 태그를 찾아줌
print(rankingnews_boxs.next_sibling.next_sibling)

# for rankingnews_boxs in rankingnews_boxs:
#   print(rankingnews_boxs.find('strong',{'class':'rankingnews_name'}))