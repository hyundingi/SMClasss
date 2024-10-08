import datetime

# 날짜, 시간, 밀리초
today = datetime.datetime.now()
print(today)     

# 날짜 포맷
now_date =  today.strftime('%Y-%H-%d')                
now_datetime = today.strftime('%Y-%m-%d %H:%M:%S') 
print(now_date)
print(type(now_date))
print(now_datetime)