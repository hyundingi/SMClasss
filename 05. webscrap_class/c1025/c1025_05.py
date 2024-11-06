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

smtpName = 'smtp.naver.com'
smtpPort = 587

# id, pw, 받는사람이메일주소
sendEmail = 'qo0723@naver.com'
pw = '1111'
recvEmail = 'bhj0723@gmail.com'

title = '제목 : 파이썬 이메일보내기 안내'
content = '''\
  파이썬에서 text 이메일을 보냅니다.\
  여러줄 쓰기 형태로 보내열
  네이버 smtp서버를 사용해서 보냄
  '''

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


