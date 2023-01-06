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


# result = [r] # 메모리오류


def dfs(start):
    global cnt
    visited[start] = cnt
    graph[start].sort()
    for i in graph[start]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)


dfs(r)
for i in range(1, n + 1):
    print(visited[i])
    # if i in result: 메모리 초과
    #     print(result.index(i) + 1)
    # else:
    #     print(0)
