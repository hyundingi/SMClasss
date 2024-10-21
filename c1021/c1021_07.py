import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}

res = requests.get(url,headers=headers)
res.raise_for_status

# html 전체를 가져옴
soup = BeautifulSoup(res.text, 'lxml')
cont = soup.find('div',{'class':'rankingnews_box_wrap'})
# print('개수확인 : ',len(rankList))

# 언론사 이름 
#print('언론사명 : ',cont.find('strong',{'class':'rankingnews_name'}).text)

rankListt = cont.find_all('div',{'class':'rankingnews_box'})
rankList = cont.find('div',{'class':'rankingnews_box'})
for t in rankListt:
  print()
  print('언론사 : ',t.find('strong',{'class':'rankingnews_name'}).text)
  ranktitle = rankList.find('ul',{'class':'rankingnews_list'}).find_all('li')
  for ii,tt in enumerate(ranktitle):
    print(ii+1,')',tt.find('a'))


# 파일에 한 줄씩 저장
# with open('c1021/news.txt','w',encoding='utf-8') as f:
#   for t in rankListt:
#     f.write('')
#     f.write(f"언론사 : {t.find('strong',{'class':'rankingnews_name'}).text}\n")
#     for ii,tt in enumerate(ranktitle):
#       f.write(f"{int(ii)+1}){tt.find('a').text}\n")
