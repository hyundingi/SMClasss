# flight.html 금액이 50000원 미만 항공권 출력
# 김포 - 제주 / 개수 : 00개
# 제주 - 김포 / 개수 : 00개

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
import random
from bs4 import BeautifulSoup
url = 'https://flight.naver.com/'

# 페이지 열기
browser = webdriver.Chrome()
browser.maximize_window()  # 창 최대화
browser.get(url)

# 출발지 선택
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[1]/b')
time.sleep(1)
elem.click()

elem = browser.find_element(By.CLASS_NAME, 'autocomplete_input__qbYlb')
elem.send_keys('김포')
time.sleep(1)
elem.click()

elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]')
time.sleep(1)
elem.click()

# 도착지 선택
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[2]/b')
time.sleep(1)
elem.click()

elem = browser.find_element(By.CLASS_NAME, 'autocomplete_input__qbYlb')
elem.send_keys('제주')
time.sleep(1)
elem.click()

elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]')
time.sleep(1)
elem.click()

# 가는날선택
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]')
time.sleep(1)
elem.click()

elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[4]')
time.sleep(1)
elem.click()

# 돌아오는 날 선택
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[7]')
time.sleep(1)
elem.click()

# 인원선택
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[3]/button')
time.sleep(1)
elem.click()

elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[4]/div/div/div[1]/div[1]/button[2]')

# 항공권 검색 버튼 클릭
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button[1]')
elem.click()
elem.click()

# 데이터를 검색하는 동안 대기 상태
time.sleep(7)

# 화면 대기 함수
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# 화면 대기 30초
# elem = WebDriverWait(browser,30).until(EC.presence_of_all_elements_located(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div[2]'))

# 현재 스크롤 높이 검색
prev_height = browser.execute_script('return document.body,scrollHeight')
print('최초 높이 : ', prev_height)

# 화면 스크롤 내리기
while True:
  browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
  time.sleep(2) # 밑에 있는 정보가 뜰 때까지 대기
  # 현재 높이 재확인
  curr_height = browser.execute_script('return document.body.scrollHeight')
  if prev_height == curr_height:  # 이제 더 밑에 정보가 안 뜬다는 뜻
    break
  else:
    prev_height = curr_height
    print('현재 높이 : ', curr_height)


