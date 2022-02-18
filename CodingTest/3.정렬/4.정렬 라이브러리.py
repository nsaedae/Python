"""
날짜 : 2022/02/18
이름 : 김철학
내용 : 코딩테스트 정렬 라이브러리 실습
"""
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# sorted
sorted_array1 = sorted(array)
print('sorted_array1 :', sorted_array1)

sorted_array2 = sorted(array, reverse=True)
print('sorted_array2 :', sorted_array2)

# sort
array.sort()
print('sorted_array3 :', array)

array.sort(reverse=True)
print('sorted_array4 :', array)

# key 매개변수를 활용한 정렬
dataset = [['바나나', 2], ['사과', 5], ['당근', 3]]

def setting(data):
    return data[1]

result1 = sorted(dataset, key=setting)
print('result1 :', result1)

result2 = sorted(dataset, key=lambda data:data[1])
print('result2 :', result2)