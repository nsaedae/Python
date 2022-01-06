def plus(x, y):
    return x+y

def minus(x, y):
    return x-y

def multi(x, y):
    return x*y

def div(x, y):
    return x/y

# 모듈의 시작점 : 모듈이 다른 모듈에 선언될때 의도하지 않는 실행로직을 차단
if __name__=='__main__':

    print('calc 모듈 실행...')

    result = plus(1, 9)
    print('resul :', result)