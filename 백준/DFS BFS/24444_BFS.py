from collections import deque
import sys

sys.setrecursionlimit(10 ** 9)
input1 = sys.stdin.readline

# 차례대로 정점의 수 , 간선의 수 , 시작 정점.
n, m, r = map(int, input1().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input1().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)
cnt = 1


def bfs(start):
    global cnt
    queue = deque([r])

    visited[r] = 1

    while queue:
        v = queue.popleft()
        graph[v].sort()
        for i in graph[v]:
            if visited[i] == 0:
                cnt +=1
                queue.append(i)
                visited[i] += cnt

bfs(r)

for i in range(1, n + 1):
    print(visited[i])
