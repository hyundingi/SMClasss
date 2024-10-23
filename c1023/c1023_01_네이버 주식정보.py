import os
import requests
import csv
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료
# print(res.text)
soup = BeautifulSoup(res.text,"lxml")

# 기준점 
data = soup.select_one('#contentarea > div.box_type_l > table')
stocks = data.select('tr')
print(len(stocks))

# 1. list (리스트 내포) :: 상단 타이틀 ------------------------------------
st_list = [st.text for st in stocks[0].select('th')]
print(st_list)  # 항목 12개

# list (for문 사용)
# for st in sts:
#   print(st.text)
#   st_list.append(st)

# 상단 타이틀 csv 저장
f = open('c1023/stock.csv','w',encoding='utf-8-sig',newline='')
writer = csv.writer(f)
writer.writerow(st_list)


# 2. 내용 ----------------------------------------------------------------
# print(len(stocks[1].select('td')))  # 항목 1개 (빈 여백)
# print(len(stocks[2].select('td')))  # 항목 12개

# sto_list = [sto.text.strip().replace('\t','').replace('\n','') for sto in stocks[2].select('td')]
# sto_list = [sto.text.strip().replace('\t','').replace('\n','') for sto in stocks[3].select('td')]
# print(sto_list)

# 30개 주식정보를 csv 파일로 저장
sto_lists = []
for s in range(2,32):
  sto_list = []
  sto = stocks[s].select('td')
  if len(sto) <= 1: continue
  for ii in range(len(sto)):
    sto_list.append(sto[ii].text.strip().replace('\t','').replace('\n',''))
  sto_lists.append(sto_list)
  writer.writerow(sto_list)
print(sto_lists)
  
# ---------- 선생님 슬랙 ----------------------
# import os
# import requests
# from bs4 import BeautifulSoup
# import time
# url = "https://finance.naver.com/sise/lastsearch2.naver"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
#     'Accept-Language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
# res = requests.get(url,headers=headers)
# res.raise_for_status() # 에러시 종료
# soup = BeautifulSoup(res.text,"lxml")
# # 기준점
# data = soup.select_one('#contentarea > div.box_type_l > table')
# stocks = data.select("tr")
# # 1.상단타이틀.
# st_list = [ st.text  for st in stocks[0].select("th") ]
# # 30개 주식정보를 csv파일로 저장하시오.
# print(len(stocks)) # 50개
# for stock in stocks:
#   sts = stock.select("td")
#   if len(sts) <= 1: continue
#   sto_list = [ st.text.strip().replace("\t","").replace("\n","")  for st in sts ]
#   print(sto_list)
# list생성
# sts = stocks[0].select("th")
# st_list = []
# for st in sts:
#   print(st.text)
#   st_list.append(st.text)
# print(st_list)  
