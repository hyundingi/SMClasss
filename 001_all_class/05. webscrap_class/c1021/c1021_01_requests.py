# 웹스크래핑 세팅
import requests
res = requests.get('http://www.google.com/')  #html 코드를 가져옴
res = requests.get('http://www.naver.com/')  #html 코드를 가져옴
# res = requests.get('http://www.melon.com/')  #html 코드를 가져옴
res.raise_for_status()  # 에러 시 종료

# request 정보를 가져올 시 
# 제이쿼리, 자바스크립트, 외부페이지(아이프레임), react, vue .. 등 비동기식으로 작동되는 소스는 가져오지 못함

# print(res.text)  # 가져온 html소스 출력
print('총 문자 길이 : ', len(res.text))

# 웹 소스코드 파일 저장 
# 1. f.close()  해야함
# f = open('a.html','w',encoding='utf-8')
# f.write(res.text)
# f.close()

# 2. close 안 해도 자동으로 닫힘
# with open('c1021/a.html','w',encoding='utf-8') as f:
#   f.write(res.text)

# --------------------------------------------------------------
# if res.status_code == 200:
#   print(res.text)
# else:
#   print('접근할 수 없습니다.')

# print('응답코드 : ', res.status_code)   # 200  #406