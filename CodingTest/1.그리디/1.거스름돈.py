"""
날짜 : 2022/02/04
이름 : 김철학
내용 : 코딩테스트 그리디 알고리즘 실습
"""
n = 1260
count = 0

array = [500, 100, 50, 10]

for coin in array:
    count += n // coin
    n %= coin

print(count)