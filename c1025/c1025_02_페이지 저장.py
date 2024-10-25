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
import csv

# selenium 화면 숨기기
Options = Options()
Options.add_argument('--headless')
Options.add_argument('--window-size=1920,1080')
Options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36')


# 제목, 금액, 평점, 평가수, 찜 정보를 1-5페이지까지 가져와서 
# 평점 4.8이상, 평가수 1000명 이상 인 상품 출력 // csv 파일로 저장 후 출력
# for i in range(1,5+1):
#   url = f'https://search.shopping.naver.com/search/all?adQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&origQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&pagingIndex={i}&pagingSize=40&productSet=total&query=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&sort=rel&timestamp=&viewType=list'
#   browser = webdriver.Chrome()
#   browser.maximize_window()
#   browser.get(url)
#   time.sleep(2)

#   pre_height = browser.execute_script('return document.body.scrollHeight')
#   while True:
#     pyautogui.scroll(-pre_height)
#     time.sleep(2)

#     curr_height = browser.execute_script('return document.body.scrollHeight')
#     if pre_height == curr_height:
#       break
#     pre_height = curr_height

#   soup = BeautifulSoup(browser.page_source, 'lxml')
#   with open(f'c1025/navershop{i}.html', 'a', encoding='utf-8') as f:
#     f.write(soup.prettify())

with open('c1025/navershop1.html','r',encoding='utf-8') as f:
  soup = BeautifulSoup(f, 'lxml')
  
  # 기준점
  data = soup.select_one('#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div')
  prods = data.select('div.product_item__MDtDF')+data.select('div.adProduct_item__1zC9h')
  print(len(prods))
  for prod in prods:
    try:
      title = prod.select_one('.product_link__TrAac')['title']
      price = prod.select_one('.price_num__S2p_v > em').text.strip()
      rating = prod.select_one('span.product_grade__IzyU3 > span').next.next.strip()
      review = prod.select_one('div.product_etc_box__ElfVA > a > em').text.replace('(','').replace(')','').strip()
      zzim = prod.select_one('div.product_etc_box__ElfVA > span:nth-child(2) > span').text.strip()
      print('상품명 : ',title)
      # print('상품명 : ',title)
      # print('가격 : ',price)
      # print('별점 : ',rating)
      # print('리뷰 수 : ',review)
      # print('찜 수 : ',zzim)
    except:
      print('프로모션 상품입니다.')

   


# with open('c1025/')
