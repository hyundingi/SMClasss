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

# 출발지 열기
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[1]/b').click()
# 출발지 입력 (김포)
elem = browser.find_element(By.CLASS_NAME, 'autocomplete_input__qbYlb').send_keys('김포')
# 김포 선택
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]')
time.sleep(1)
elem.click()

time.sleep(2)

# 도착지 열기
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[2]/b').click()
# 도착지 입력 (제주)
elem = browser.find_element(By.CLASS_NAME, 'autocomplete_input__qbYlb').send_keys('제주')
# 제주 선택
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]')
elem.click()

time.sleep(2)

# 가는날 - 달력열기
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]').click()
# 가는 날짜 선택
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[4]')
time.sleep(1)
elem.click()
# 돌아오는 날짜 선택
elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[7]')
elem.click()

time.sleep(2)

# 인원선택
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[3]/button').click()
# 인원 1명 추가
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[4]/div/div/div[1]/div[1]/button[2]')
elem.click()
time.sleep(2)

# 항공권 검색
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button[1]')
time.sleep(1)
elem.click()
elem.click()

# 데이터를 검색하는 동안 대기 상태
# 검색중 
time.sleep(7)
# ------------------------------------
# 화면대기함수
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 화면 대기 -30초 동안
# 화면에 찾으려고 하는 html요소가 있는 지 확인
# elem = WebDriverWait(browser,30).until(EC.presence_of_all_elements_located(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div[2]'))

# 현재 스크롤 높이 검색
prev_height = browser.execute_script('return document.body.scrollHeight')
print('최초 높이 : ', prev_height)

# 화면 스크롤 내리기
while True:
  browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
  time.sleep(2) # 다른 정보가 추가될 때까지 대기
  # 현재 높이 다시 확인
  curr_height = browser.execute_script('return document.body.scrollHeight')
  if prev_height == curr_height:
    break
  else:
    prev_height = curr_height
    print('현재 높이 : ', curr_height)


# 데이터 가져와서 처리 
# beautifulSoup 데이터 처리
# 웹 스크래핑
soup = BeautifulSoup(browser.page_source, 'lxml')
with open('c1023/flight.html','w',encoding='utf-8') as f:
  f.write(soup.prettify())

input('enter키를 입력하면 프로그램이 종료됩니다.')
browser.quit()




# 네이버 항공권 사이트 들어가기
# elem = browser.find_element(By.ID, 'query')
# elem.send_keys('네이버 항공권')
# elem.send_keys(Keys.ENTER)
# elem = browser.find_element(By.CLASS_NAME, 'link_name')
# elem.click()

time.sleep(100)