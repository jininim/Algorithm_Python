from collections import deque

m, n = map(int, input().split())  # 가로 세로
graph = []
cnt = 0
for _ in range(n):
    graph.append(list(map(int, input().split())))
# deque 라이브러리 사용
queue = deque()
# 익은 토마토의 인덱스를 queue에 저장.
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))

# 이동할 네 방향 정의(상,하,좌,우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# bfs 함수 정의
def bfs():
    while queue:  # 큐가 비어있지 않으면 실행
        x, y = queue.popleft()
        for i in range(4):  # 상하좌우 위치 확인
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간을 벗어난 경우 무시
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue

            # 이동 좌표에 토마토가 익지 않았을 경우
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx, ny))


bfs() # bfs 함수 실행
for i in graph:
    for j in i:
        if j == 0: # 익지 않은 토마토가 있을경우 -1 출력
            print(-1)
            exit(0)
    cnt = max(cnt,max(i))
# 시작 값 빼주기
print(cnt-1)



