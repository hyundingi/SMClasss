import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get('https://daum.net')

# 다음 사이트에서 주식정보를 검색해서 페이지 이동 ----------------------
elem = browser.find_element(By.ID, 'q')
elem.send_keys('주식정보')
elem.send_keys(Keys.ENTER)

browser.get('http://www.naver.com')
elem = browser.find_element(By.CLASS_NAME, 'search_input')
elem.send_keys('주식정보')
time.sleep(3)
elem.send_keys(Keys.ENTER)

time.sleep(100)








# print(random.uniform(1,3))

# for 문과 한줄for문
# a = [0]*100
# for i in range(100):
#   a[i] = i
# print(a)

# b = [i for i in range(100)]
# # # print(b)

# for i in b:
#   print(i)
#   time.sleep(random.uniform(1,3))





