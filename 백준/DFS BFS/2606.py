# dfs 사용
n = int(input())  # 컴퓨터의 수
m = int(input())  # 간선의 수
graph = [[] * n for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [False] * (n + 1)


def dfs(start):
    global cnt
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            cnt += 1


dfs(1)
print(cnt)
