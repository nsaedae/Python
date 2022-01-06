"""
날짜 : 2022/01/06
이름 : 김철학
내용 : 파이썬 파일 입출력 실습하기 교재 p217
"""

# 파일읽기
f1 = open('./Test.txt', mode='r', encoding='utf-8')

while True:
    # 줄 단위로 읽기
    line = f1.read()

    if not line:  # 읽을 줄이 없으면
        break

    print(line)

f1.close()

# 파일쓰기
f2 = open('./Result.txt', mode='w', encoding='utf-8')
f2.write('안녕하세요.\n')
f2.write('반갑습니다.\n')
f2.write('감사합니다.\n')
f2.close()

# 구구단 쓰기
f3 = open('./Gugudan.txt', mode='w', encoding='utf-8')

for x in range(2, 10):
    f3.write('%d단\n' % x)
    for y in range(1, 10):
        z = x * y
        f3.write('{} x {} = {}\n'.format(x, y, z))

f3.close()

