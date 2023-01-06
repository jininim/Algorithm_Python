from collections import deque
import sys

read = sys.stdin.readline
n, m, v = map(int, read().split())  # 정점 , 간선 , 시작정점
graph = [[] * n for _ in range(n + 1)]
visited = [False] * (n + 1)
for i in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(len(graph)): # 작은것부터 순회하기 때문에 그래프에 노드별로 오름차순 정렬.
    graph[i].sort()


# dfs 함수 정의
def dfs(start):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(i)


# bfs 함수 정의
def bfs(start):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    while queue:
        q = queue.popleft()
        print(q, end=" ")
        for i in graph[q]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

#출력
dfs(v)
print()
bfs(v)
