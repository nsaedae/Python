"""
날짜 : 2022/01/04
이름 : 김철학
내용 : 파이썬 기본 입출력
"""

# 이름, 나이, 생년월일 출력
name = input("이름을 입력하시오 : ")
age  = input("나이를 입력하시오 : ")

year = 2021 - int(age)
year = str(year)

print(name+'님은 '+age+'세이고, '+year+'년도에 태어났습니다.')