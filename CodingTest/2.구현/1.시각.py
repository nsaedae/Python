"""
날짜 : 2022/02/11
이름 : 김철학
내용 : 코딩테스트 구현 실습
"""

n = int(input())

count = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            time = str(h) + str(m) + str(s)
            if '3' in time:
                count += 1

print(count)



