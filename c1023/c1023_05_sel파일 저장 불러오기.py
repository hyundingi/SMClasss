from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup

# 파일 불러와서 저장하기 - 1회
for i in range(1,5):
  url = f'https://www.yeogi.com/domestic-accommodations?keyword=%EA%B0%95%EB%A6%89&checkIn=2024-10-23&checkOut=2024-10-24&personal=2&freeForm=false&page={i}'
  browser = webdriver.Chrome()
  browser.get(url)  # 이동하려는 주소 입력
  # time.sleep(3)
  soup = BeautifulSoup(browser.page_source,'lxml')
  # 파일 저장
  with open(f'c1023/yeogi{i}.html','w',encoding='utf-8') as f:
    f.write(soup.prettify())


# 파일을 불러와서 beatifulsoup 으로 파싱(변환)
for a in range(1,5):
  with open(f'c1023/yeogi{a}.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f,'lxml')
    # 숙박명 별점 평가수 가격 이미지 링크주소
    # 기준점
    data = soup.select_one('#__next > div > main > section > div.css-1qumol3')
    sells = data.select('a')
    # 내용
    print(f'[강릉 숙소 페이지{a}]')
    for idx, sell in enumerate(sells):
      try:
        rate = sell.select_one('.css-9ml4lz').text.strip()
        rate = float(rate)
        num = sell.select_one('span.css-oj6onp').text.strip()[:-4]
        num = int(num.replace(',',''))
        price = sell.select_one('div.css-yeouz0 > span.css-5r5920').text.strip()
        price = int(price.replace(',',''))
        if rate >=9.0 and num>=500 and price < 120000:
          print(idx+1,'.')
          print('상품명 : ',sell.select_one('.css-8fn780 > h3').text.strip())
          print('별점 : ',rate)
          print('리뷰수 : ',num)
          print('가격 : ',price)
          #print('이미지 링크 : ',sell.select_one('div.css-nl3cnv'))
          print(f'바로가기 : https://www.yeogi.com/{sell['href']}')
      except Exception as e:
        print(idx,'예외처리 ', e)


# time.sleep(100)

# request로 정보 가져오기
# url = 'https://www.yeogi.com/domestic-accommodations?keyword=%EA%B0%95%ED%99%94%EB%8F%84&autoKeyword=&checkIn=2024-11-09&checkOut=2024-11-10&personal=3&freeForm=true'
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36', 
#            'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}

# res = requests.get(url, headers=headers)
# soup = BeautifulSoup(res.text, 'lxml')

# with open('c1023/yeogi1.html','w',encoding='utf-8') as f:
#   f.write(soup.prettify())

# data = soup.select_one('#__next > div > main > section > div.css-1qumol3')