from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import random
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import pyautogui

# url = 'https://new.land.naver.com/complexes?ms=37.4592802,126.8930386,17&a=APT:PRE:ABYG:JGC&e=RETAIL'

# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get(url)

# pyautogui.moveTo(1270,550)
# time.sleep(1)
# pyautogui.moveTo(1270,500)
# pyautogui.click()
# time.sleep(1)
# pyautogui.moveTo(200,780)
# time.sleep(1)

# # all_height = browser.execute_script('return document.body.scrollHeight')
# # print('화면 전체 높이 : ', all_height)

# prev_height = browser.execute_script('return articleListArea.scrollHeight')
# print('화면 높이 : ', prev_height)

# while True:
#   # browser.execute_script('window.scroll(0, articleListArea.scrollHeight)')
#   pyautogui.scroll(-prev_height)
#   time.sleep(1)
#   curr_height = browser.execute_script('return articleListArea.scrollHeight')
#   if prev_height == curr_height:
#     break
#   prev_height = curr_height
#   print('높이 : ', prev_height)

# soup = BeautifulSoup(browser.page_source, 'lxml')
# data = soup.select_one('#complexOverviewList > div.list_content > div.item_area > div')
# with open('c1024/naver.html','w',encoding='utf-8') as f:
#   f.write(soup.prettify())

# 매매 가격 낮은 5개, 전세 가격 낮은 5개

with open('c1024/naver.html','r',encoding='utf-8') as f:
  soup = BeautifulSoup(f, 'lxml')

  # 기준점
  data = soup.select_one('#articleListArea')
  apts = data.select('.item_inner')
  print(len(apts))
  Apts = []
  mm_list = []
  js_list = []
  for i in range(len(apts)):
    apts_title = apts[i].select_one('.item_title > .text').text.strip()
    apts_type = apts[i].select_one('.price_line > .type').text.strip()
    apts_price = apts[i].select_one('.price_line > .price').text.strip().replace('\n','').replace(',','').split('억')

    if apts_type != '월세':
      apts_price[0] =  int(apts_price[0]) * 1000000000
      if apts_price[1] == '':
        del apts_price[1]
      else:
        apts_price[1] = int(apts_price[1] ) * 10000
        apts_price[0] = apts_price[0] + apts_price[1]
    else:
      apts_price[0] = '월세 제외'
      
    apt = [i, apts_title, apts_type, apts_price[0]]
    Apts.append(apt)
    if apt[2] == '매매':
      mm_list.append(apt)
    elif apt[2] == '전세':
      js_list.append(apt)


# 리스트 출력
# for ii in Apts:
#   try:
#     print(ii[0],'.')
#     print(f'분류 : {ii[1]}')
#     print(f'타입 : {ii[2]}')
#     print(f'금액 : {ii[3]:,}원')
#   except:
#     print('월세 제외')


# 정렬
mm_list.sort(key=lambda x:x[3], reverse=True)
print(mm_list[:5])
print('[매매 리스트]')
for mm in mm_list[:5]:
  print(mm[0],'.')
  print('매물명 : ',mm[1])
  print('타입 : ', mm[2])
  print(f'금액 : {mm[3]:,}')
  print('-'*50)
js_list.sort(key=lambda x:x[3], reverse=True)
print('[전세 리스트]')
for js in js_list[:5]:
  print(js[0],'.')
  print('매물명 : ',js[1])
  print('타입 : ', js[2])
  print(f'금액 : {js[3]:,}')
  print('-'*50)


# input('엔터키 입력 완료')

