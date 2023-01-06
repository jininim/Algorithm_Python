from collections import deque

t = int(input())  # 테스트 케이스
dx = [-2, -2, 2, 2, 1, 1, -1, -1]
dy = [-1, 1, -1, 1, 2, -2, 2, -2]  # 8가지 방향 정의


def bfs():  # bfs 함수정의

    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx >= l or ny >= l or nx < 0 or ny < 0:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


for _ in range(t):  # 테스트 케이스 만큼 반복
    queue = deque()
    l = int(input())
    graph = [[0] * l for i in range(l)]  # l*l 리스트 생성
    a, b = map(int, input().split())  # 시작 지점
    c, d = map(int, input().split())  # 목적지
    if (a, b) == (c, d): # 출발지점과 목적지가 같다면 0 출력
        print(0)
        continue
    queue.append((a, b)) # queue에 시작지점 저장
    bfs() # bfs 실행
    print(graph[c][d]) # 정답출력
