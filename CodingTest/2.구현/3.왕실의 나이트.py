"""
날짜 : 2022/02/11
이름 : 김철학
내용 : 코딩테스트 구현 왕실의 나이트 실습
"""

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

result = 0

# 오른쪽 2칸, 위쪽 1칸
next_row = row - 1
next_column = column + 2

if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1

# 오른쪽 2칸, 아래쪽 1칸
next_row = row + 1
next_column = column + 2

if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1

# 왼쪽 2칸, 위쪽 1칸
next_row = row - 1
next_column = column - 2

if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1

# 왼쪽 2칸, 아래쪽 1칸
next_row = row + 1
next_column = column - 2

if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1

# 위쪽 2칸, 오른쪽 1칸
next_row = row - 2
next_column = column + 1

if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1

# 위쪽 2칸, 왼쪽 1칸
next_row = row - 2
next_column = column - 1

if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1

# 아래쪽 2칸, 오른쪽 1칸
next_row = row + 2
next_column = column + 1

if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1


# 아래쪽 2칸, 왼쪽 1칸
next_row = row + 2
next_column = column - 1

if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1


print(result)