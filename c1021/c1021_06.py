import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}

res = requests.get(url,headers=headers)
res.raise_for_status

soup = BeautifulSoup(res.text, 'lxml')

# 타이틀 5개 찾기

# newList = soup.find('div',{'class':'rankingnews_box_wrap'}).find_all('div',{'class':'rankingnews_box'})
# for newList in newList[0:5]:
#   print(newList.find('strong',{'class':'rankingnews_name'}))
newlist = soup.find('div',{'class':'rankingnews_box_wrap'}).find('div',{'class':'rankingnews_box'})
newList = newlist.find('strong',{'class':'rankingnews_name'})
print('타이틀 : ', newList.text)
newLList = newlist.find('ul',{'class':'rankingnews_list'}).find_all('li')
# print(newLList)
for i,t in enumerate(newLList):
  print(i+1,':',t.find('a').text)
