"""
날짜 : 2022/03/11
이름 : 김철학
내용 : 코딩테스트 - 순차탐색
"""

# 순차탐색 함수
def sequential_search(dataset, target):
    pos = -1

    for i in range(len(dataset)):
        if dataset[i] == target:
            pos = i
            break

    return pos

dataset = [5, 10, 18, 22, 35, 55, 75, 103, 152]

value = int(input('검색할 숫자 : '))
pos = sequential_search(dataset, value)

if pos == -1:
    print('찾을려는 숫자가 없습니다.')
else:
    print('%d는 %d번째에 있습니다.' % (value, pos+1))



