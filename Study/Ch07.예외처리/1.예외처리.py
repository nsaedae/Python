"""
날짜 : 2022/01/06
이름 : 김철학
내용 : 파이썬 예외처리 실습하기 교재 p212
"""
print('start...')

# try ~ except
num1, num2 = 1, 0

r1 = num1 + num2
r2 = num1 - num2
r3 = num1 * num2
r4 = 0

try:
    # 예외(에러)가 발생할 가능성이 있는 코드 작성
    r4 = num1 / num2
except:
    # 예외가 발생했을 때 처리할 코드 작성
    print('예외발생...')

print('r1 :', r1)
print('r2 :', r2)
print('r3 :', r3)
print('r4 :', r4)

# try ~ except ~ finally
animal = ['Tiger', 'Eagle', 'Shark']
result = None

while True:
    try:
        print('Animal을 선택하세요.')
        print('1:호랑이, 2:독수리, 3:상어, 0:종료')

        answer = int(input('선택 : '))

        if answer == 0:
            break

        result = animal[answer-1]

    except Exception as e:
        print('에러내용 :', e)
    finally:
        # 에러발생 여부와 상관없이 마지막 무조건 실행코드 블럭
        if result != None:
            print('선택한 동물은 %s입니다.' % result)

print('finish...')