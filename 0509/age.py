import datetime

name = input('이름입력 : ')
year = int(input('출생 연도 입력 : '))
now = datetime.datetime.now()
age = now.year - year
print('당신의 나이는', age, ' 입니다.')
