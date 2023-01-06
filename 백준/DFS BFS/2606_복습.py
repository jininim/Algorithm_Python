# 컴퓨터의 수
from pprint import pprint

n = int(input())
# 연결되어 있는 컴퓨터 쌍의 수
m = int(input())

graph = [[] * n for _ in range(n + 1)]  # 리스트 생성
# [         [],
#  1번노드   [2, 5],
#  2번노드   [1, 3, 5],
#  3번노드   [2],
#  4번노드   [7],
#  5번노드  [1, 2, 6],
#  6번노드   [5],
#  7번노드  [4]
#     ]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [False] * (n + 1)


def dfs(start):
    global cnt
    # 첫 번째 노드 방문처리
    visited[start] = True
    print(start)
    for i in graph[start]:
        # i번째 노드를 방문하지 않았다면
        if not visited[i]:
            # i번째 노드 dfs 실행
            dfs(i)
            # cnt 1 증가
            cnt += 1


# 1 번째 노드 dfs 실행
dfs(1)
# 정답 출력
print(cnt)
