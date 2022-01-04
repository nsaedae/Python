"""
날짜 : 2022/01/04
이름 : 김철학
내용 : 파이썬 자료구조 List 실습하기 교재 p84
"""

# 리스트
list1 = [1, 2, 3, 4, 5]

print('list1 type :', type(list1))
print('list1[0] :', list1[0])
print('list1[2] :', list1[2])
print('list1[3] :', list1[3])

list2 = [5, 3.14, True, 'Apple']
print('list2 type :', type(list2))
print('list2[1] :', list2[1])
print('list2[2] :', list2[2])
print('list2[3] :', list2[3])

list3 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

print('list3 type :', type(list3))
print('list3[0][2] :', list3[0][2])
print('list3[1][1] :', list3[1][1])
print('list3[2][0] :', list3[2][0])

# 리스트 수정, 추가, 삭제
dataset = [1, 2, 3, 4, 5]
print('dataset :', dataset)

dataset[1] = 7
print('dataset :', dataset)

dataset[2:4] = [8, 9, 10]
print('dataset :', dataset)

dataset[3:5] = []
print('dataset :', dataset)

# 리스트 반복문
for num in [1, 2, 3, 4, 5]:
    print('num :', num)

people = ['김유신', '김춘추', '장보고']

for person in people:
    print('person :', person)

for index, value in enumerate(people):
    print('%d-%s' % (index, value))

# 리스트 Comprehension
array = [1, 2, 3, 4, 5]

result1 = [num * 3 for num in array]
result2 = [num * 3 for num in array if num % 2 == 1]

print('result1 :', result1)
print('result2 :', result2)