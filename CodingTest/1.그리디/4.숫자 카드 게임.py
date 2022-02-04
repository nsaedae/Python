"""
날짜 : 2022/02/04
이름 : 김철학
내용 : 코딩테스트 그리디 알고리즘 실습
"""
n, m = map(int, input().split())

result = 0
mins = []

for i in range(n):
    data = list(map(int, input().split()))

    # data에서 가장 작은수
    data.sort()
    min = data[0]
    mins.append(min)

mins.sort(reverse=True)

# mins에서 가장 큰값
result = mins[0]

print(result)