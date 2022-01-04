"""
날짜 : 2022/01/03
이름 : 김철학
내용 : 파이썬 3장 연습문제 교재 p77
"""

"""[문제1]"""
"""[문제2] while 반복문을 이용한 '숫자 맞추기 게임' """
import random

print('>>숫자 맞추기 게임<<')
com = random.randint(1, 10)

while True:
    my = int(input('예상 숫자 입력 : '))

    if my == com:
        print('~~성공~~')
        break

    if my > com:
        print('더 작은 수 입력')
        continue

    if my < com:
        print('더 큰 수 입력')
        continue

"""[문제3]"""
"""[문제4]"""