n, m = map(int, input().split())  # 세로 가로 크기 입력
x, y, d = map(int, input().split())  # x,y에서 d 방향을 바라 보고 서있음.
mapp = [[0] * m for _ in range(n)]  # 방문한 위치를 저장 하기 위해 맵을 생성 하여 0으로 초기화
array = [list(map(int, input().split())) for _ in range(n)]  # 리스트 컴프리헨션
mapp[x][y] = 1  # 현재 좌표 방문 처리

# 북 동 남 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽으로 회선 turn_left 함수 정의
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3


# 시뮬레이션 시작
cnt = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[d]
    ny = x + dy[d]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if mapp[nx][ny] == 0 and array[nx][ny] == 0:
        mapp[nx][ny] = 1  # 현재 좌표 방문 처리
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0
print(cnt)
