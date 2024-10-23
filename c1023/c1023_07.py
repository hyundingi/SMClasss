from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
import random
from bs4 import BeautifulSoup

url = 'https://www.daum.net'
browser = webdriver.Chrome()
browser.get(url)

elem = browser.find_element(By.CLASS_NAME, 'btn_login')
time.sleep(random.randint(2,5))
elem.click()

id = 'qo0723@naver.com'
pw = 'gktehrm99'
input_js = 'document.getElementById("loginId--1").value = "{}";\
  document.getElementById("password--2").value = "{}";'.format(id,pw)

browser.execute_script(input_js)
time.sleep(random.randint(2,5))
elem = browser.find_element(By.CLASS_NAME, 'btn_g')
elem.click()

time.sleep(100)
