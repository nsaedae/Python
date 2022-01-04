"""
날짜 : 2022/01/03
이름 : 김철학
내용 : 파이썬 반복문 for 실습하기 교재 p70
"""

# for문
for i in range(5):
    print('반복 i :', i)

for j in range(10, 20):
    print('반복 j :', j)

for k in range(10, 0, -1):
    print('반복 k :', k)


# 1부터 10까지 합
tot = 0

for k in range(11):
    tot += k

print('1부터 10까지 합 :', tot)

# 1부터 10까지 짝수합
sum = 0

for k in range(11):
    if k%2 == 0:
        sum += k

print('1부터 10까지 짝수합 :', sum)

# 중첩 for
for a in range(3):
    print('a :', a)
    for b in range(4):
        print('b :', b)
        for c in range(5):
            print('c :', c)

# 구구단
for x in range(2, 10):
    print('%d단' % x)
    for y in range(1, 10):
        z = x * y
        print('{} x {} = {}'.format(x, y, z))

# 별삼각형
for start in range(1, 11):

    for end in range(11-start):
        print('☆', end='')

    print()  # 줄바꿈

for i in range(11):
    print('★' * i)

