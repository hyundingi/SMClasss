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

# selenium 화면 숨기기
Options = Options()
Options.add_argument('--headless')
Options.add_argument('--window-size=1920,1080')
Options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36')

url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
browser = webdriver.Chrome(options=Options)
browser.maximize_window()
browser.get(url)

soup = BeautifulSoup(browser.page_source, 'lxml')
data = soup.select_one('#detected_value').text
print('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36')
print('-'*50)
print(data)

# 화면 캡쳐
browser.get_screenshot_as_file('gmarket.png')



# # gmarket 1,2,3 페이지 html로 저장 
# for i in range(1,3+1):
#   url = f'https://www.gmarket.co.kr/n/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&k=61&p={i}'
#   browser = webdriver.Chrome()
#   browser.maximize_window()
#   browser.get(url)
#   time.sleep(3)
#   soup = BeautifulSoup(browser.page_source, 'lxml')
#   with open(f'c1024/gmarket{i}.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())

input('엔터키 입력 완료')

# # 파일 불러오기
# for i in range(1,3+1):
#   with open(f'c1024/gmarket{i}','r',encoding='utf-8') as f:
#     soup = BeautifulSoup(f, 'lxml')
