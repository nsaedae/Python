"""
날짜 : 2022/01/03
이름 : 김철학
내용 : 파이썬 조건문 if 실습하기 교재 p60
"""

# if문
num1, num2 = 1, 2

if num1 > 0:
    print('num1은 0보다 크다.')

if num1 > num2:
    print('num1은 num2보다 크다.')

if num1 > 0:
    if num2 > 1:
        print('num1은 0보다 크고, num2는 1보다 크다.')

if num1 > 0 and num2 > 1:
    print('num1은 0보다 크고 그리고 num2는 1보다 크다.')

# if ~ else
num3, num4 = 3, 4

if num3 > num4:
    print('num3은 num4보다 크다.')
    pass # 코드블럭을 비워둘때 사용하는 키워드
else:
    print('num3은 num4보다 작다.')
    pass

# if ~ elif ~ else
if num1 > num2:
    print('num1은 num2보다 크다.')
elif num2 > num3:
    print('num2은 num3보다 크다.')
elif num3 > num4:
    print('num3은 num4보다 크다.')
else:
    print('num4가 가장 크다.')
