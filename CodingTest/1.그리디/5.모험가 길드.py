"""
날짜 : 2022/04/01
이름 : 김철학
내용 : 코딩테스트 그리디 - 모험가 길드
"""
n = int(input())
data = list(map(int,input().split()))

data.sort()

# 그룹 수
result = 0

# 한 그룹당 인원수
count = 0

for i in data:
    count += 1
    
    # 현재 인덱스의 모험가는 그룹의 인원수로 먼저 포함
    # 그룹의 인원 수는 현재 인덱스의 공포도보다 같거나 커야 그룹으로 인정
    if count >= i:
        result += 1
        count = 0

print(result)