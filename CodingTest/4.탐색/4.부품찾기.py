"""
날짜 : 2022/03/11
이름 : 김철학
내용 : 코딩테스트 - 부품 찾기
"""
from bisect import bisect_left

def BinarySearch(dataset, target):
    i = bisect_left(dataset, target)
    if dataset[i] == target:
        return i
    else:
        return -1

# N(부품 갯수) 입력
n = int(input())

# 가게에 있는 전체 부품 번호를 공백 구분해서 입력
dataset = list(map(int, input().split()))
# 이진탐색 전 정렬은 필수 수행
dataset.sort()

# M(손님이 요청한 부품 갯수) 입력
m = int(input())

# 손님이 요청한 부품번호 공백 구분해서 입력
requests = list(map(int, input().split()))

# 손님이 요청한 부품번호를 하나씩 확인
for num in requests:
    # 해당 부품이 존재하는지 확인
    result = BinarySearch(dataset, num)
    if result == -1:
        print('no', end=' ')
    else:
        print('yes', end=' ')

