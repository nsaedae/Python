"""
날짜 : 2022/01/06
이름 : 김철학
내용 : 파이썬 패키지와 모듈 실습하기 교재 p175

패키지 : 모듈파일이 있는 폴더
모듈 : 파이썬 파일(확장자 py)
"""
from Study.Lib.calc import *
import Study.Lib.calc as c

r1 = plus(1, 2)
r2 = minus(1, 2)
r3 = c.multi(2, 3)
r4 = c.div(8, 2)

print('r1 :', r1)
print('r2 :', r2)
print('r3 :', r3)
print('r4 :', r4)




