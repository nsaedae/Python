"""
날짜 : 2022/03/25
이름 : 김철학
내용 : 코딩테스트 - 6.다이나믹 프로그래밍 피보나치 하향식(재귀식+메모이제이션 이용)
"""
import time

# 프로그램 실행 시간!
start_time = time.time()

# DP(Dynamic Programming) 테이블(메모이제이션을 위한 리스트)
d = [0] * 10000

# 피보나치 함수
def fibo(n):
    if n <= 1:
        return n

    if d[n] != 0:
        return d[n]

    d[n] = fibo(n-1) + fibo(n-2)

    return d[n]



for i in range(10000):
    print(fibo(i), end=' ')

print()

# 프로그램 종료 시간!
end_time = time.time()

# 전체 실행 시간
total_time = end_time - start_time
print('프로그램 실행시간 :', total_time)

