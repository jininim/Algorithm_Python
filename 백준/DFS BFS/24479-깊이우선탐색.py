# DFS 메서드 정의
def dfs(graph, r, visited):
    # 현재 노드를 방문 처리
    visited[r] = True
    print(r)
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[r]:
        if not visited[i]:  # 노드를 방문 하지 않았다면 실행
            dfs(graph, i, visited)


n, m, r = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))
visited = [False] * (n + 1)
dfs(graph, r, visited)
