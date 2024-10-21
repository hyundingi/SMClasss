import requests
from bs4 import BeautifulSoup

url = 'https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}
res = requests.get(url, headers=headers)
res.raise_for_status()

# soup 변환
soup = BeautifulSoup(res.text, 'lxml')

print(soup.find('div',{'id':'bestPrdList'}).find('h3').text)
best = soup.find('div',{'id':'bestPrdList'}).find('ul',{'class':'cfix'}).find_all('li')

for i, best in enumerate(best):
  print(i+1,':',best.find('p').text)
  print('가격 : ', best.find('strong').text)