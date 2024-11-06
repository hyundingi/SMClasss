import requests
from bs4 import BeautifulSoup

# for i in range(2020,2024):
#   url = f'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&q={i}%EB%85%84+%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84'
#   headers = {'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
#             'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
#   res = requests.get(url,headers=headers)
#   res.raise_for_status()

#   with open(f'd1106/movie{i}.html','w',encoding='utf-8-sig') as f:
#     f.write(res.text)

# --------- 데이터 가져오기
movie_lists = []
for r in range(2020,2024):
  with open(f'd1106/movie2022.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f,'lxml')

  # 1. 2020년 ~ 2023년 영화 제목 / 관객수 : 숫자입력 / 날짜 이미지저장
  #Data = soup.select_one('#morColl')
  Data = soup.select_one('#mor_history_id_0')
  movies_title = Data.select('c-title')
  movies_view = Data.select('c-contents-desc')
  movies_date = Data.select('c-contents-desc-sub')


  for i in range(len(movies_title)):
    movie_list = []
    m_t = movies_title[i].next.strip()
    m_v = movies_view[i].next.replace('누적','').replace('만명','0000').replace(',','').strip()
    m_d = movies_date[i].next.strip()


    movie_list = [r, m_t, int(m_v), m_d]
    movie_lists.append(movie_list)
    
print(movie_lists)

