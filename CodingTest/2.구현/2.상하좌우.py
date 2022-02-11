"""
날짜 : 2022/02/11
이름 : 김철학
내용 : 코딩테스트 구현 상하좌우 실습
"""
n = int(input())
x, y = 1, 1
plans = input().split()

for plan in plans:
    if plan == 'L':
        if y == 1:
            continue
        else:
            y -= 1

    if plan == 'R':
        if y == n:
            continue
        else:
            y += 1

    if plan == 'U':
        if x == 1:
            continue
        else:
            x -= 1

    if plan == 'D':
        if x == n:
            continue
        else:
            x += 1

# 최종 좌표 출력
print(x, y)

