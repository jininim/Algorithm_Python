from collections import deque
import sys

# 정점의 개수 , 간선의 개수 , 시작 정점 입력 받기
read = sys.stdin.readline
n, m, v = map(int, read().split())
# 2차원 리스트 graph
graph = [[] * n for _ in range(n + 1)]
# 간선이 연결하는 두 정점의 번호 입력받기
for _ in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)
# graph 오름차순 정렬
for i in range(len(graph)):
    graph[i].sort()
# [
#     [],
#     [1, 2, 3],
#     [1, 4],
#     [1, 4],
#     [2, 3, 4]
# ]
visited = [False] * (n + 1)


# def 함수 정의
def dfs(v):
    # 시작노드 방문처리, 방문순서 대입
    visited[v] = True
    print(v,end=' ')
    # 방문 순서 출력
    for i in graph[v]:
        # i노드를 방문하지 않았다면
        if not visited[i]:
            # i노드 dfs 실행
            dfs(i)


# bfs 함수 정의
def bfs(v):
    visited = [False] * (n + 1)
    queue = deque([v])
    visited[v] = True
    while queue:
        r = queue.popleft()
        print(r, end=' ')
        for i in graph[r]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# dfs,bfs 실행
dfs(v)
print()
bfs(v)
