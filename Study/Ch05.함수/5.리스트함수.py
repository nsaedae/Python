"""
날짜 : 2022/01/06
이름 : 김철학
내용 : 파이썬 리스트함수 실습하기 교재 p88
"""
import math

dataset = [1, 4, 3]
print(dataset)

# 데이터 추가
dataset.append(2)
dataset.append(5)
print(dataset)

# 데이터 정렬
dataset.sort()
print(dataset)

dataset.sort(reverse=True)
print(dataset)

# 데이터 뒤집기
dataset.reverse()
print(dataset)

# 데이터 삽입
dataset.insert(2, 6)
print(dataset)

dataset.insert(1, 7)
print(dataset)

# 데이터 삭제
dataset.remove(6) # 값으로 삭제
print(dataset)

dataset.pop(1) # 인덱스로 삭제
print(dataset)

# map함수 : 리스트의 모든 원소를 지정한 함수로 처리해는 함수
def plus10(x):
    return x+10

list1 = [1, 2, 3, 4, 5]
r1 = map(plus10, list1)
r1 = list(r1)
print('r1 :', r1)

list2 = [0.1, 1.2, 2.6, 3.4, 4.9]
r2 = list(map(math.ceil, list2))
print('r2 :', r2)

list3 = ['10', '20', '30', '40', '50']
r3 = list(map(int, list3))
print('r3 :', r3)
