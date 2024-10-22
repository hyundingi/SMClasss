import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/lastsearch2.naver'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status() 

soup = BeautifulSoup(res.text, 'lxml')

titles = soup.select('tr.type1 > th')
names = soup.select('a.tltle')
Datas = soup.select('td.number')
print(Datas)

for Data in Datas:
  pure = Data.text.replace(',','').replace('%','').replace('.','')
  if int(pure) == TypeError and int(pure) == ValueError:
    print(Data.text, end = '\t')
 

# for title in titles:
#   print(title.text, end='\t')
# for name in names:
#   print(name.select_one('a'))
# Data = name.find_next_siblings('td')
# print(name)
