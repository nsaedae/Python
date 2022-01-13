"""
날짜 : 2022/01/13
이름 : 김철학
내용 : 파이썬 데이터베이스 프로그래밍 교재 p295
"""
import pymysql

# 데이터베이스 접속
conn = pymysql.connect(host='54.180.160.240',
                       user='test',
                       password='1234',
                       db='test',
                       charset='utf8')

# SQL실행 객체 생성(Cursor)
cur = conn.cursor()

# SQL실행
sql = "DELETE FROM `User1` WHERE `uid`='p101';"
cur.execute(sql)
conn.commit()

# 데이터베이스 종료
conn.close()

print('Delete 완료...')
