"""
날짜 : 2022/01/06
이름 : 김철학
내용 : 파이썬 함수 고급 실습하기 교재 p129
"""

# 디폴트 매개변수
def hello(name='홍길동', age=21):
    print('%s님 반갑습니다.\n올해 나이는 %d세 입니다.' % (name, age))

hello('김유신', 25)
hello('김춘추')
hello()

# 하나 이상의 리턴값
def sum_and_multi(n1, n2):
    y1 = n1 + n2
    y2 = n1 * n2
    return y1, y2

r1, r2 = sum_and_multi(1, 2)
r3, r4 = sum_and_multi(2, 3)

print('r1, r2 :', r1, r2)
print('r3, r4 :', r3, r4)

# 변수에 저장하는 함수
def plus(x, y):
    return x+y

def minus(x, y):
    return x-y

var1 = plus
var2 = minus

y1 = var1(1, 2)
y2 = var2(1, 2)

print('y1 :', y1)
print('y2 :', y2)

cals = [plus, minus]

res1 = cals[0](2, 3)
res2 = cals[1](4, 3)

print('res1 :', res1)
print('res2 :', res2)

# 람다함수(익명함수)
lam1 = lambda x, y: x + y
lam2 = lambda x, y: x - y

rs1 = lam1(10, 11)
rs2 = lam2(10, 11)

print('rs1 :', rs1)
print('rs2 :', rs2)
