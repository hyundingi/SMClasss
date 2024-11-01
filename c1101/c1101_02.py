import datetime

nowYear = datetime.datetime.now().year

in_year = input('생년월일 입력')
print(f'현재 나이 : {nowYear-int(in_year[:4])}')


