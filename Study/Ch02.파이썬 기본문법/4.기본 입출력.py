"""
날짜 : 2021/12/31
이름 : 김철학
내용 : 파이썬 기본 입출력 실습하기 교재 p42
"""

# 파이썬 기본 입력장치
num = input('숫자 입력 : ')

# 파이썬 기본 출력장치
print('입력한 num :', num)
print('num type :', type(num))

# 문자열을 숫자로 변환
num = int(num)
result = num + 1
print(result)

# 파이썬 출력 옵션
print('010', '1234', '5678', sep='-') # 구분자를 포함해서 출력
print('Hello', end='~ ') # 그 다음 출력문과 이어서 출력
print('Python', end=' ')
print('Programming')

# 서식문자
print('%d년 %d월 %d일 %s요일' % (2021, 12, 31, '금'))

# 포맷문자
print('{}년 {}월 {}일 {}요일'.format(2021, 12, 31, '금'))

