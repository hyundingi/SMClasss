import requests

# res = requests.get('http://www.google.com')
# res = requests.get('https://www.whatismybrowser.com/detect/what-is-my-user-agent/#google_vignette')

# User-Agent 크롬브라우저 정보로 변경해서 전달
url = 'http://www.melon.com'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}

res = requests.get(url,headers=headers)
#print('코드 정보 : ',res.status_code)
res.raise_for_status()

# print(res.text)

with open('c1021/b.html','w',encoding='utf-8') as f:
  f.write(res.text)