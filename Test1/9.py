"""
날짜 : 2022/01/04
이름 : 홍길동
내용 : 파이썬 팩토리얼 연습문제
"""

num = 5
result = 1

print('%d!' % num, end=' = ')

for i in range(num, 0, -1):

    result *= i

    if i > 1:
        print(i, end=' x ')
    else:
        print(i)


print('결과 :', result)
