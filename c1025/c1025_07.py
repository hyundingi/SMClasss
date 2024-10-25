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
# email 발송관련
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

url = 'https://news.naver.com/main/ranking/popularDay.naver'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

soup = BeautifulSoup(browser.page_source, 'lxml')

Data = soup.select_one('#wrap > div.rankingnews._popularWelBase._persist > div.rankingnews_box_wrap._popularRanking > div > div:nth-child(1)')
news_list = Data.select('li')

title = '네이버 뉴스 랭킹 데이터'
mailCons = []
for i in range(len(news_list)):
  mailCon = []
  newsCom = Data.select_one('a > strong').text
  newstit = news_list[i].select_one('div > a.list_title').text
  newslink = news_list[i].select_one('div > a.list_title')['href']
  mailCon = [i+1,newsCom,newstit,newslink]
  mailCons.append(mailCon)

with open('c1025/mailtext.txt','w',encoding='utf-8') as f:
  for c in mailCons:
    f.write(f'{c[0]} 번 \n')
    f.write(f'{c[1]} \n')
    f.write(f'{c[2]} \n')
    f.write(f'바로가기 링크 : {c[3]} \n')
    f.write('--------------------------------------------------------------\n')

with open('c1025/mailtext.txt','r',encoding='utf-8') as f:
  content = f.read()
  
smtpName = 'smtp.naver.com'
smtpPort = 587

# id, pw, 받는사람이메일주소
sendEmail = 'qo0723@naver.com'
pw = 'xhfpxk99'
recvEmail = 'bhj0723@gmail.com'

# 설정
msg = MIMEText(content)
msg['Subject'] = title
msg['From'] = sendEmail
msg['To'] = recvEmail

print('msg 데이터 : ',msg.as_string())

# 서버이름, 서버포트
s = smtplib.SMTP(smtpName, smtpPort)
s.starttls()
s.login(sendEmail, pw)
s.sendmail(sendEmail, recvEmail, msg.as_string())
s.quit()

# 메일 발송 완료
print('메일발송완료')