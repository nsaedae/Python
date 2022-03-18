"""
날짜 : 2022/03/18
이름 : 김철학
내용 : 그래프 탐색 BFS(너비 우선 탐색) 실습
"""
from collections import deque

# 그래프 표현
graph = [[],
         [2, 3, 8],
         [1, 7],
         [1, 4, 5],
         [3, 5],
         [3, 4],
         [7],
         [2, 6, 8],
         [1, 7]]

# 큐를 이용한 bfs
def bfs(graph, start_node):
    visited = []

    queue = deque([start_node])
    visited.append(start_node)

    while queue:
        current = queue.popleft()

        for x in graph[current]:  # 현재노드의 인접노드 탐색
            if x not in visited:  # 인접노드에 방문하지 않았으면
                queue.append(x)   # 인접노드 큐 저장
                visited.append(x) # 인접노드 방문처리

    return visited

# bfs 실행
visited = bfs(graph, 1)
print(visited)

