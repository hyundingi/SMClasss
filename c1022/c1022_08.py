import os
import requests
from bs4 import BeautifulSoup
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=9&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료
# print(res.text)
soup = BeautifulSoup(res.text,"lxml")

# 상품명, 가격, 평점, 평가인원, 링크주소, 이미지주소
# 기준점
data = soup.select_one('ul#productList').select('li.search-product')

# 금액 90만원 이상 / 평점 4.5 이상 / 리뷰수 500개 이상 - 리스트에 저장
n_lists = []
for i in range(len(data)):
    n_list = [] # 상품명, 금액, 평점, 평가수, 링크, 이미지
    try:
        price = data[i].select_one('strong.price-value').text.strip().replace(',','')
        rate = float(data[i].select_one('em.rating').text)
        review = int(data[i].select_one('span.rating-total-count').text[1:-1])
        name = data[i].select_one('div.name').text
        img_link = 'http:'+data[i].select_one('img')['src']
        link = 'https://www.coupang.com/'+data[i].select_one('a.search-product-link')['href']
        if int(price) >=900000 and rate >= 4.5 and review >= 500:
            print(i+1,'상품명 : ', data[i].select_one('div.name').text)
            if data[i].select_one('strong.price-value').text.strip() != "":
                print(f'가격 : {int(data[i].select_one('strong.price-value').text.strip().replace(',','')):,}')
            else:
                print('가격 정보 없음')

            if data[i].select_one('em.rating').text != None:
                print('평점 : ', data[i].select_one('em.rating').text)
            else:
                print('리뷰없음')

            print('리뷰수 : ', data[i].select_one('span.rating-total-count').text[1:-1])
            print(f'이미지 주소 : https:{data[i].select_one('img')['src']}', end='\n')
            print(f'상품 주소 : https://www.coupang.com/{data[i].select_one('a.search-product-link')['href']}', end='\n')
            print()
            a = name, price, rate, review, link, img_link
            n_list.append(a)
            n_lists.append(n_list)

        #n_lists.append(n_list)
    except Exception as e:
        print('에러', e)

for i in n_lists:
    print(i, end='\t')