def solution(maps):
    n = len(maps)  # 맵의 행 수
    m = len(maps[0])  # 맵의 열 수

    # 이동할 네 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 최단 경로를 찾는 BFS 함수
    def bfs(x, y):
        queue = [(x, y, 1)]  # 시작 위치와 이동 횟수를 큐에 추가
        visited = set()  # 방문한 위치를 저장하는 집합

        while queue:
            x, y, count = queue.pop(0)  # 큐에서 위치와 이동 횟수를 가져옴

            # 현재 위치가 도착점이면 최단 경로를 찾은 것이므로 이동 횟수 반환
            if x == n - 1 and y == m - 1:
                return count

            # 현재 위치에서 네 방향으로의 위치 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 맵을 벗어난 경우 무시
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                # 벽이거나 이미 방문한 곳인 경우 무시
                if maps[nx][ny] == 0 or (nx, ny) in visited:
                    continue

                # 방문한 위치를 집합에 추가
                visited.add((nx, ny))

                # 다음 위치와 이동 횟수를 큐에 추가
                queue.append((nx, ny, count + 1))

        # 도착점에 도달할 수 없는 경우 -1 반환
        return -1

    # 시작 위치 (0, 0)에서 BFS 호출
    return bfs(0, 0)