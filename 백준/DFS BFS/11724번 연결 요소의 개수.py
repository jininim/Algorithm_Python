import sys

sys.setrecursionlimit(10 ** 6)


# dfs 함수 정의
def dfs(start):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i)


# 정점의 개수 n , 간선의 개수 m
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
cnt = 0
visited = [False] * (n + 1)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    if not visited[i]:
        if not graph[i]:
            cnt += 1
            visited[i] = True
        else:
            dfs(i)
            cnt += 1
print(cnt)
