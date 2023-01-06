import sys
sys.setrecursionlimit(10**6)
t = int(input())  # 테스트 케이스


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 1:  # 방문하지 않았으면
        graph[x][y] = 0  # 방문 표시
        dfs(x - 1, y)  # 좌
        dfs(x + 1, y)  # 우
        dfs(x, y - 1)  # 상
        dfs(x, y + 1)  # 하
        return True
    return False


for _ in range(t):
    # 가로길이 , 세로길이 , 배추가 심어져 있는 위치의 개수
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    result = 0
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1 # x가 가로축 y가 세로축
    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                result += 1
    print(result)
