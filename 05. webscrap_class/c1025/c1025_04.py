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

with open('c1025/navershop1.html','r',encoding='utf-8') as f:
  soup = BeautifulSoup(f, 'lxml')

  # 기준점
  data = soup.select_one('#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div')
  # 광고 상품 리스트 (4개)
  # pro_lists = data.select('.adProduct_item__1zC9h')
 
 # csv 파일 저장
  f = open('c1025/nshop.csv','a',encoding='utf-8-sig', newline='')
  writer = csv.writer(f)

  # for i, pro_list in enumerate(pro_lists):
  #   try:
  #     print(i+1,'.')
  #     # 상품명
  #     title = pro_list.select_one('div.adProduct_title__amInq > a')['title'].strip()
  #     print(title)
  #     # 금액
  #     price = int(pro_list.select_one('div.adProduct_info_area__dTSZf > div.adProduct_price_area__yA7Ad > strong > span.price > span.price_num__S2p_v > em').text.strip().replace(',',''))
  #     print(price)
  #     # 별점
  #     rating = float(pro_list.select_one('div.adProduct_etc_box__UJJ90 > span:nth-child(1) > a > span.adProduct_rating__PaMzh').text.strip())
  #     print(rating)
  #     # 평가수
  #     a_count = int(pro_list.select_one('div.adProduct_etc_box__UJJ90 > span:nth-child(1) > a > em').text.replace(',','').strip())
  #     print(a_count)
  #     # 찜
  #     c_count = int(pro_list.select_one('div.adProduct_etc_box__UJJ90 > span:nth-child(2) > span').text.replace(',','').strip())
  #     print(c_count)
  #     print('-'*50)

  #     writer.writerow([title,price,rating,a_count,c_count])
  #   except:
  #     print('에러')

  # 일반 판매상품 (40개)
  pro_lists = data.select('.product_item__MDtDF')
  # csv 파일저장
  f = open('c1025/nshop.csv','a',encoding='utf-8-sig',newline="")
  writer = csv.writer(f)
  for pro_list in pro_lists:
    try:
      title = pro_list.select_one('.product_link__TrAac')['title'].strip()
      print(title)
      # 금액
      price = int(pro_list.select_one('.price_num__S2p_v > em').text.strip().replace(',',''))
      print(price)
      # 별점
      rating = float(pro_list.select_one('span.product_grade__IzyU3').text.replace('\n','').strip()[2:])
      print(rating)
      # 평가수
      a_count = pro_list.select_one('div.product_etc_box__ElfVA > a > em').text.replace(',','').replace('(','').replace('\n','').strip()[1:-1]
      if '만' in a_count:
        a_count = float(a_count[:-1])*10000
      else:
        float(a_count)
      print(a_count)
      # 찜
      c_count = int(pro_list.select_one("div.product_etc_box__ElfVA > span:nth-child(2) > span").text.replace(",","").strip())
      print(c_count)
      print('-'*50)
      writer.writerow([title,price,rating,a_count,c_count])
    except:
      print("예외처리")
  
  f.close()


