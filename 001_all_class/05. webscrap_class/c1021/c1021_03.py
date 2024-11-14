# naver , 리솜리조트 파일 저장

import requests

# url = 'http://www.naver.com'
# url2 = 'https://www.resom.co.kr/forest/main/main.asp'
# url3 = 'https://www.coupang.com/'

# url = [
#   'http://www.naver.com',
#   'http://www.resom.co.kr/forest/main/main.asp',
#   'http://www.daum.net/',
#   'http://www.coupang.com/'
# ]

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}
# for i in range(len(url)):
#   res = requests.get(url[i],headers=headers)
#   res.raise_for_status()

#   # 파일 저장
#   with open(f"c1021/{i}.html",'w',encoding='utf-8') as f:
#     f.write(res.text)

# res = requests.get(url,headers=headers)
# res2 = requests.get(url2,headers=headers)

# with open('c1021/naver.html','w',encoding='utf-8') as f:
#   f.write(res.text)
# with open('c1021/resom.html','w',encoding='utf-8') as f:
#   f.write(res2.text)



url3 = 'http://www.coupang.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}
res = requests.get(url3,headers=headers)
res.raise_for_status()
print(res.text)
# 파일 저장
with open("c1021/cupang.html",'w',encoding='utf-8') as f:
  f.write(res.text)
