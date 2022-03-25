"""
날짜 : 2022/03/25
이름 : 김철학
내용 : 코딩테스트 - 6.다이나믹 프로그래밍 피보나치 상향식(반복문 이용)
"""
import time

# 프로그램 실행 시간!
start_time = time.time()

# DP(Dynamic Programming) 테이블
d = [0] * 10000
d[0] = 0
d[1] = 1

# 피보나치 반복문
for n in range(2, 10000):
    d[n] = d[n-1] + d[n-2]
    print(d[n], end=' ')

print()

# 프로그램 종료 시간!
end_time = time.time()

# 전체 실행 시간
total_time = end_time - start_time
print('프로그램 실행시간 :', total_time)

