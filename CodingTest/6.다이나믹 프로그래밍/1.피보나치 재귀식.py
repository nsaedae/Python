"""
날짜 : 2022/03/25
이름 : 김철학
내용 : 코딩테스트 - 6.다이나믹 프로그래밍
"""
import time

# 프로그램 실행 시간!
start_time = time.time()

# 피보나치 함수
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)


for i in range(40):
    print(fibo(i), end=' ')

print()



# 프로그램 종료 시간!
end_time = time.time()

# 전체 실행 시간
total_time = end_time - start_time
print('프로그램 실행시간 :', total_time)

