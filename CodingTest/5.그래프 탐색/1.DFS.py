"""
날짜 : 2022/03/18
이름 : 김철학
내용 : 그래프 탐색 DFS(깊이 우선 탐색) 실습
"""

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

# 스택을 이용한 DFS
def stack_dfs(graph, start_node):
    visited = []
    stack = []

    stack.append(start_node)
    visited.append(start_node)

    while stack:
        current = stack[-1]
        last = graph[current][-1]

        for x in graph[current]:  # 현재노드의 인접노드 탐색
            if x not in visited:  # 인접노드가 방문하지 않았으면
                stack.append(x)   # 인접노드 스택저장
                visited.append(x) # 인접노드 방문처리
                break
            elif x == last:       # 현재노드의 인접노드가 마지막 노드이면
                stack.pop()

    return visited

# 재귀함수를 이용한 dfs
def recursive_dfs(graph, node, visited):
    visited.append(node)
    print(node, end=' ')

    for n in graph[node]:
        if n not in visited:
            recursive_dfs(graph, n, visited)


# dfs 실행 1
visited = stack_dfs(graph, 1)
print(visited)

# dfs 실행 2
recursive_dfs(graph, 1, visited=[])















