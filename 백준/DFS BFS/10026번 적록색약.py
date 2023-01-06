import copy
import sys
sys.setrecursionlimit(10**6)

n = int(input())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(sys.stdin.readline()))
# copy 라이브러리를 통해 리스트 복사
graph2 = copy.deepcopy(graph)
result = 0
result2 = 0


#dfs red
def dfs_r(x, y):  # dfs 함수 정의
    # 주어진 범위를 벗어나는 경우에는 즉시종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == "R":
        # 해당 노드를 방문 처리
        graph[x][y] = "O"
        # 상,하,좌,우의 위치도 모두 재귀적으로 호출
        dfs_r(x - 1, y)  # 상
        dfs_r(x, y - 1)  # 좌
        dfs_r(x + 1, y)  # 하
        dfs_r(x, y + 1)  # 우
        return True
    return False


# dfs green
def dfs_g(x, y):  # dfs 함수 정의
    # 주어진 범위를 벗어나는 경우에는 즉시종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == "G":
        # 해당 노드를 방문 처리
        graph[x][y] = "O"
        # 상,하,좌,우의 위치도 모두 재귀적으로 호출
        dfs_g(x - 1, y)  # 상
        dfs_g(x, y - 1)  # 좌
        dfs_g(x + 1, y)  # 하
        dfs_g(x, y + 1)  # 우
        return True
    return False


# dfs blue
def dfs_b(x, y):  # dfs 함수 정의
    # 주어진 범위를 벗어나는 경우에는 즉시종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == "B":
        # 해당 노드를 방문 처리
        graph[x][y] = "O"
        # 상,하,좌,우의 위치도 모두 재귀적으로 호출
        dfs_b(x - 1, y)  # 상
        dfs_b(x, y - 1)  # 좌
        dfs_b(x + 1, y)  # 하
        dfs_b(x, y + 1)  # 우
        return True
    return False

# 적록색맹인 경우 Blue dfs
def dfs_b2(x, y):  # dfs 함수 정의
    # 주어진 범위를 벗어나는 경우에는 즉시종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph2[x][y] == "B":
        # 해당 노드를 방문 처리
        graph2[x][y] = "O"
        # 상,하,좌,우의 위치도 모두 재귀적으로 호출
        dfs_b2(x - 1, y)  # 상
        dfs_b2(x, y - 1)  # 좌
        dfs_b2(x + 1, y)  # 하
        dfs_b2(x, y + 1)  # 우
        return True
    return False

# 적록색맹일때 dfs
def dfs_rg(x, y):  # dfs 함수 정의
    # 주어진 범위를 벗어나는 경우에는 즉시종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph2[x][y] == "R" or graph2[x][y] == "G":
        # 해당 노드를 방문 처리
        graph2[x][y] = "O"
        # 상,하,좌,우의 위치도 모두 재귀적으로 호출
        dfs_rg(x - 1, y)  # 상
        dfs_rg(x, y - 1)  # 좌
        dfs_rg(x + 1, y)  # 하
        dfs_rg(x, y + 1)  # 우
        return True
    return False


for i in range(n):
    for j in range(n):
        # 현재 위치에서 DFS
        if dfs_b2(i, j):
            result2 += 1
        if dfs_rg(i, j):
            result2 += 1
        if dfs_r(i, j):
            result += 1
        if dfs_b(i, j):
            result += 1
        if dfs_g(i, j):
            result += 1


print(result, result2)
