"""
날짜 : 2022/02/04
이름 : 김철학
내용 : 코딩테스트 그리디 알고리즘 실습
"""
n, k = map(int, input().split())

result = 0

while True:

    if n == 1:
        break

    if n % k != 0:
        # 1빼기
        n -= 1
    else:
        # k로 나누기
        n /= k

    result += 1

print(result)