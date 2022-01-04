"""
날짜 : 2022/01/03
이름 : 김철학
내용 : 파이썬 문자열 실습하기 교재 p48
"""

# 문자열 더하기
str1 = 'Hello'
str2 = 'Python'
str3 = str1 + str2

print('str3 :', str3)

# 문자열 곱하기
hello = '안녕'
result = hello * 3
print('result :', result)

# 문자열 길이
text = 'Hello World'
size = len(text)
print('size :', size)

# 문자열 인덱스
print('text 1번째 문자 :', text[0])
print('text 7번째 문자 :', text[6])
print('text -1번째 문자 :', text[-1])

# 문자열 자르기
print('text 0~5까지 문자열 :', text[0:5])
print('text 처음~5까지 문자열 :', text[:5])
print('text 6~11까지 문자열 :', text[6:11])
print('text 6~마지막까지 문자열 :', text[6:])

# 문자열 분리
people = '김유신,김춘추,장보고,강감찬,이순신'
p1, p2, p3, p4, p5 = people.split(',')

print('p1 :', p1)
print('p2 :', p2)
print('p3 :', p3)
print('p4 :', p4)
print('p5 :', p5)

# 문자열 이스케이프
print('서울\n대전\n대구\n부산\n광주')
print('서울\t대전\t대구\t부산\t광주')
print('안녕하세요. \'반갑습니다.\'')
print("안녕하세요. '반갑습니다.'")
