"""
날짜 : 2022/03/11
이름 : 김철학
내용 : 코딩테스트 - 이진탐색 라이브러리 함수
"""

from bisect import bisect_left

dataset = [5, 10, 18, 22, 35, 55, 75, 103, 152]
value = int(input('검색할 숫자 : '))

pos = bisect_left(dataset, value)
print('pos :', pos)

def binary_search(dataset, target):
    i = bisect_left(dataset, target)
    if dataset[i] == target:
        return i
    else:
        return -1

value = int(input('검색할 숫자 : '))
pos = binary_search(dataset, value)

if pos == -1:
    print('찾을려는 숫자가 없습니다.')
else:
    print('%d는 %d번째에 있습니다.' % (value, pos+1))