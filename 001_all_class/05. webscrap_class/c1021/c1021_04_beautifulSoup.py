import requests
from bs4 import BeautifulSoup

url = 'https://n.news.naver.com/article/025/0003394670?ntype=RANKING'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status()

with open('c1021/11.html','w',encoding='utf-8') as f:
  f.write(res.text)

# str(res.text) 이지만 html, css 정보를 가진 소스로 변경
soup = BeautifulSoup(res.text,'lxml')  # str > html태그, css태그 사용될 수 있는 형태로 변경

# BeautifulSoup 사용 ---------------------------------------------------------------------------------------------------------------
# 태그 출력, 태그 글자 출력
print(soup.title)                 # title 태그를 가져옴 :  <title>"9년 만에 세계관 완성"…조세호 결혼식에 등장한 '깜짝 손님'</title>
print(soup.title.text)            # title 태그 안에 있는 문자를 가져옴 : "9년 만에 세계관 완성"…조세호 결혼식에 등장한 '깜짝 손님'
print(soup.title.get_text())      # title 태그 안에 있는 문자를 가져옴 : "9년 만에 세계관 완성"…조세호 결혼식에 등장한 '깜짝 손님'

print('에러태그 : ', soup.titletitle)  # 없는 태그 입력시 None
# print('없는 태그 : ', soup.titletitle.get_text())  # 없는 태그의 겟_텍스트 시 에러 발생


print(soup.span)                    # span 태그 첫번째 것을 가져옴
print(soup.span.next.text)          # span 태그 다음 줄을 가져옴

# 태그 속성 출력 -------------------------------------------------------------------------------------------------------------------
print(soup.span.attrs)             # 태그의 속성값을 가져옴 : 딕셔너리 형태
print(soup.span['class'])          # 태그의 class 속성값을 가져옴

# 특정정보 출력 --------------------------------------------------------------------------------------------------------------------
print(soup.find('span',attrs={'class':'ofhd_float_title_text_press'}))
print(soup.find('span',{'class':'ofhd_float_title_text_press'}))

# soup = BeautifulSoup(res.text,'lxml')
# with open('c1021/22.html','w',encoding='utf-8') as f:
#   f.write(soup.prettify())

print('완료')

# print(res.text)