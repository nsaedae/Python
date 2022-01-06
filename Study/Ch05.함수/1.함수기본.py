"""
날짜 : 2022/01/06
이름 : 김철학
내용 : 파이썬 함수 실습하기 교재 p114
"""

# 함수 : 일련의 코드로직을 재활용하기 위해 모듈화한 코드 블럭
def f(x):
    y = 2 * x + 3
    return y

# 함수호출
y1 = f(1)
y2 = f(2)
y3 = f(3)

print('y1 :', y1)
print('y2 :', y2)
print('y3 :', y3)

# 함수유형1 - 매개변수 O, 리턴값 O
def type1(x, y):
    z = x + y
    return z

r1 = type1(1, 2)
r2 = type1(1.1, 2.1)
r3 = type1('Hello', 'World')

print('r1 :', r1)
print('r2 :', r2)
print('r3 :', r3)

# 함수유형2 - 매개변수 O, 리턴값 x
def type2(dataset):
    tot = 0
    for data in dataset:
        tot += data

    print('dataset 합 :', tot)

type2([1, 2, 3, 4, 5])
type2((1, 3, 5, 7, 9))

# 함수유형3 - 매개변수 x, 리턴값 O
def type3():
    dataset = [n for n in range(11)]

    tot = 0
    for k in dataset:
        tot += k

    return tot

result = type3()
print('type3 결과 :', result)

# 함수유형4 - 매개변수 x, 리턴값 x
def type4():
    type2([x for x in range(11) if x % 2 == 0])

type4()

