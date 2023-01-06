import sys
from collections import deque


def bfs(v):
    queue = deque([v])
    while queue:
        v = queue.popleft()
        # 수빈이와 동생의 위치가 같다면
        if v == k:
            return visited[v]

        for x in (v - 1, v + 1, 2 * v):
            if 0 <= x < MAX + 1 and not visited[x]:
                visited[x] = visited[v] + 1
                queue.append(x)


MAX = 10 ** 5
n, k = map(int, sys.stdin.readline().split())
visited = [0] * (MAX + 1)

print(bfs(n))