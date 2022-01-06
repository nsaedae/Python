"""
날짜 : 2022/01/06
이름 : 김철학
내용 : 파이썬 내장함수 실습하기 교재 p118
"""
import math
import random
import time

# 시간 관련 함수
t1 = time.time()
print('t1 :', t1)  # Unix time

t2 = time.ctime()
print('t2 :', t2)  # 변환된 Unix time

now   = time.localtime(time.time())
year  = time.strftime('%Y', now)
month = time.strftime('%m', now)
date  = time.strftime('%d', now)
hour  = time.strftime('%H', now)
min   = time.strftime('%M', now)
sec   = time.strftime('%S', now)

print('{}년 {}월 {}일 {}:{}:{}'.format(year, month, date, hour, min, sec))

# 수학 관련 함수
r1 = math.ceil(1.2)  # 올림함수
r2 = math.ceil(1.8)

print('r1 :', r1)
print('r2 :', r2)

r3 = math.floor(1.2) # 내림함수
r4 = math.floor(1.8)

print('r3 :', r3)
print('r4 :', r4)

r5 = round(1.2)  # 반올림
r6 = round(1.8)

print('r5 :', r5)
print('r6 :', r6)

# Random : 임의의 수를 구하는 함수
num1 = random.random()
print('num1 :', num1) # 0 ~ 1사이의 임의의 실수

num2 = num1 * 10
print('num2 :', num2) # 0 ~ 10사이의 임의의 실수

num3 = math.ceil(num2)
print('num3 :', num3) # 1 ~ 10사이의 임의의 정수

result = math.ceil(random.random()*10)
print('1에서 10사이의 임의의 정수 :', result)
