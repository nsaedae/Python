"""
날짜 : 2020/12/22
이름 : 김철학
내용 : 파이썬 입력함수 실습하기
"""

# 입력함수
num = input('숫자 입력 : ')

# 출력함수
print('num : ', num)


def grade(score):
    if 90 <= score <= 100:
        print('A 입니다.')
    elif 80 <= score < 90:
        print('B 입니다.')
    elif 70 <= score < 80:
        print('C 입니다.')
    elif 60 <= score < 70:
        print('D 입니다.')
    else:
        print('F 입니다.')


while True:
    score = input('점수 입력(종료는 -1) : ')

    # 입력받은 문자열을 숫자로 변환
    score = int(score)

    if score == -1:
        break

    grade(score)

print('프로그램 종료...')