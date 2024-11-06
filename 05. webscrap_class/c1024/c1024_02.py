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

# 화면 숨김 처리
Options = Options()
Options.add_argument('--headless')
Options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36')

# 노트북으로 검색된 사이트 1,2,3 페이지에서 
# 만족도 95 이상 / 금액 150만원 이하 / 평가수 100이상 

# gmarket 1,2,3 페이지 html로 저장 
for i in range(1,3+1):
  url = f'https://www.gmarket.co.kr/n/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&k=61&p={i}'
  browser = webdriver.Chrome(options=Options)
  browser.get(url)
  browser.get_screenshot_as_file('gmarket.jpg')
  soup = BeautifulSoup(browser.page_source, 'lxml')
  with open(f'c1024/gmarket{i}.html','w',encoding='utf-8') as f:
    f.write(soup.prettify())

# html 읽어와서 찾기
# for i in range(1,3+1):
  #with open(f'c1024/gmarket{i}.html','r',encoding='utf-8') as f:
with open(f'c1024/gmarket1.html','r',encoding='utf-8') as f:
  soup = BeautifulSoup(f, 'lxml')
  # 기준점
  Data = soup.select_one('#section__inner-content-body-container')
  laps = Data.select_one('#section__inner-content-body-container > div:nth-child(2)')
  name = laps.select_one('.link__item > span.text__item').text.strip()
  rate = laps.select_one('span.for-a11y').text
  print(name)
  print(rate)

