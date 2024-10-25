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


# 네이버 쇼핑 클릭 > 쇼핑 페이지에서 무선 마우스 검색 > 엔터 
url = 'http://www.naver.com'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

# --- 네이버 쇼핑 클릭
pyautogui.moveTo(820, 270)
time.sleep(1)
pyautogui.click()
time.sleep(2)

# ---- 네이버 쇼핑에서 무선 마우스 검색
browser.switch_to.window(browser.window_handles[1])
elem = browser.find_element(By.XPATH, '//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div/input')
elem.click()
elem.send_keys('무선 마우스')
time.sleep(2)
elem.send_keys(Keys.ENTER)


