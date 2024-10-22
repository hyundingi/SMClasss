import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status() 

soup = BeautifulSoup(res.text, 'lxml')

# print(soup.select_one('h3.h_popular>span').text)

# 기준점
data = soup.select_one('#container > div.aside > div > div.aside_area.aside_popular')

# 인기검색종목
print(data.select_one('span').text)

# 1,2,3,4,5 위
pops = data.select('tbody > tr')
# for idx, pop in enumerate(pops):
#   if pop.select_one('span.blind').text == '하락':
#     print(f'{idx+1}. {pop.select_one('a').text} / {pop.select_one('td').text}원 / ⇓ {pop.select_one('span.tah').text}')

#   else:
#     print(f'{idx+1}. {pop.select_one('a').text} / {pop.select_one('td').text}원 / ⇑ {pop.select_one('span.tah').text}')
sum = 0
for idx, pop in enumerate(pops): 
  sum += int(pop.select_one('td').text.replace(',',''))
 
  # sps = pop.select_one('td').find_next_sibling('td').select('span')
 
  print(sum)

  #for sp in sps:
  # print(sp.text.strip())
  # next_sibling : 형제관계, find_next_sibling : 형제관계중 검색
  # print(f'{idx+1}. {pop.select_one('a').text} / {pop.select_one('td').text}원 / {pop.select_one('td').find_next_sibling('td').select_one('span').text.strip()}')
  # print(f'{idx+1}. {pop.select_one('a').text} / {pop.select_one('td').text}원 / {sps.next.next.next.strip()}')

