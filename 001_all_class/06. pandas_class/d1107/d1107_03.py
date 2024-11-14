from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

# 파일 저장
topTitle = ['제목','관객수','날짜']
f = open('screens.csv', 'a', encoding='utf-8')
f.write('제목,관객수,날짜\n')
# f.write('제목,관객수,날짜\n')  # 1번만 글저장

# 웹스크래핑 시작
for syear in range(2020, 2024):
  with open(f'd1107/screen{syear}.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')
    print(f'{syear}년도 -------- ')
    # 기준점
    data = soup.select_one('#mor_history_id_0')
    screens = data.select('li')
    for i, screen in enumerate(screens):
      print(f'{i+1}----------------------')
      title = screens[i].select_one('.tit-g.clamp-g').text.strip()
      s_img = screens[i].select_one('.wrap_thumb img')['src']
      number = int(screens[i].select_one('.conts-desc.clamp-g').text.strip()[3:-2].replace(',',''))
      sdate = screens[i].select_one('.conts-subdesc.clamp-g').text.strip()[:-1]
      # print('제목 : ', title)
      # print('이미지 : ', s_img)
      # print('관객 수 : ', number)
      # print('날짜 : ', sdate)

      s_list = [title,number,sdate]
      # f.writelines(s_list)
      f.write(f'{title},{number},{sdate}\n')
      print(s_list)
f.close()








# a_list = ['서울의 봄', 100, '2024-11-07']


# with open('d1107/s.txt', 'w', encoding='utf-8') as f:
#   a_title = ['제목', '관객수', '날짜']
#   f.write(','.join(a_title)+'\n')
#   for i in range(10):
#     f.write(','.join(a_list)+'\n')

# print('프로그램 완료')

# a_list = ['서울의 봄', 100, '2024-11-07']


# with open('d1107/s2.csv', 'w', encoding='utf-8') as f:
#   a_title = ['제목', '관객수', '날짜']
#   f.write(','.join(a_title)+'\n')
#   for i in range(10):
#     f.write(','.join(a_list)+'\n')

# print('프로그램 완료')
