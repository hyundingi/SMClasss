from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import random
from bs4 import BeautifulSoup

# url = 'https://www.yanolja.com/?trackcode=mkt_google_sa&utm_source=google_sa&utm_medium=cpc&utm_campaign=20738115572&utm_content=160897187931&utm_term=aud-2260605335759%3Akwd-298391364620&gad_source=1&gclid=Cj0KCQjwveK4BhD4ARIsAKy6pMJQOg7Hg9cBMb98AxiunKROHRSxzxWGcWu2VEyYY7OlUBcS92tDLLYaAgsmEALw_wcB'
# # 브라우저 열기
# browser = webdriver.Chrome()
# # 창 최대화
# browser.maximize_window()
# # url 입력
# browser.get(url)

# # 검색창 클릭
# browser.find_element(By.XPATH,'//*[@id="__next"]/div/div/header/section/a[2]/div/div').click()

# # 날짜 선택
# elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div[1]/form/div/div[2]/div[1]')
# elem.click()
# time.sleep(1)
# # 체크인 날짜
# elem = browser.find_element(By.XPATH, '/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[2]')
# elem.click()
# time.sleep(1)
# # 체크아웃 날짜
# elem = browser.find_element(By.XPATH, '/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[4]')
# elem.click()
# time.sleep(1)
# # 확인
# elem = browser.find_element(By.XPATH, '/html/body/div[4]/div/div/section/section[4]/button')
# elem.click()

# # 검색창에 글자입력
# elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div[1]/form/div/div[1]/div/input')
# elem.click()
# time.sleep(1)
# elem.send_keys('강릉 호텔')
# elem.send_keys(Keys.ENTER)
# time.sleep(7)

# # 자동시 로딩 대기 
# # 화면에 호텔 검색 내용이 뜰 때까지 대기 / 최대 30초 까지 
# WebDriverWait(browser,30).until(lambda x:x.find_element(By.XPATH, '//*[@id="__next"]/div/main/section/div[2]'))

# # 화면을 스크롤해서 내리기 반복
# # execute_script : 자바스크립트 실행 함수
# prev_height = browser.execute_script('return document.body.scrollHeight')
# while True:
#   browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
#   time.sleep(1)
#   # 페이지가 로딩되면서 길어진 길이를 다시 가져옴
#   curr_height = browser.execute_script('return document.body.scrollHeight')
#   if prev_height == curr_height:
#     break
#   # 길이가 더 길얼졌으면 , 이전 길이에 현재 길이를 입력시킴
#   prev_height = curr_height

# print('스크롤 내리기 완료')

# # 브라우저 html파일로 저장
# soup = BeautifulSoup(browser.page_source, 'lxml')
# with open('c1024/yanolja.html','w',encoding='utf-8') as f:
#   f.write(soup.prettify())

# 평점 4.8이상 / 금액 170,000원 이하 
# 1.
# 호텔명 : 
# 평점 : 
# 금액 : 
# --------
# 2. 
# 조건에 맞는 개수 :
# 조건에 맞지 않는 개수 :

# 파일 불러와서 soup으로 파싱
with open('c1024/yanolja.html', 'r', encoding='utf-8') as f:
  soup = BeautifulSoup(f, 'lxml')
  # 데이터(기준점)
  data = soup.select_one('div.PlaceListBody_listContainer__2qFG1')
  hotel = data.select('div.PlaceListItemText_container__fUIgA')
  count = 0
  countt = 0
  print('[강릉 호텔]')
  search_list = []
  for i in range(len(hotel)):
    lists = []
    try:
      hotel_name = hotel[i].select_one('a')['title']
      hotel_rate = float(hotel[i].select_one('.PlaceListScore_reviewInfo__3QSCU').previous.previous.strip())
      hotel_price = int(hotel[i].select_one('.PlacePriceInfoV2_discountPrice__1PuwK').next.strip().replace(',',''))
      
      if hotel_rate >= 4.8 and hotel_price <= 170000:
        print(i+1,'.')
        print('호텔명 : ',hotel_name)
        print('평점 : ',hotel_rate)
        print(f'금액 : {hotel_price:,}')
        print('-'*30)
        lists.append(i, hotel_name, hotel_rate, hotel_price)
        search_list.append(lists)
        count += 1
    except Exception as e:
      countt += 1
  print('조건에 맞는 개수 : ', count)
  print('조건에 맞지 않는 개수 : ', len(hotel)-count)
  print('오류 : ', countt)

# 리스트에 담고 정렬
# print(search_list)
# [1,호텔명,평점,가격]
# 평점 역순정렬
search_list.sort(key=lambda x:x[2],reverse=True)
print(search_list[:5])
# 금액 순차정렬
search_list.sort(key=lambda x:x[3])
print(search_list[:5])  

     