# 입력
n = int(input())
a = list(input().split())
x, y = 1, 1
for i in a:  # O(N)시간 복잡도 a의 길이 만큼 실행
    if i == "R" and y < n:
        y += 1
    elif i == "L" and y > 1:
        y -= 1
    elif i == "U" and x > 1:
        x -= 1
    elif i == "D" and x < n:
        x += 1
print(x, y)
# 책 풀이법
# LRUD에 따른 이동 방향.
dx = [ 0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

#이동 계획을 하나씩 확인
for plan in a:
    #이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    #공간을 벗어나는 경우 무시
    if nx<1 or ny <1 or nx >n or ny >n:
        continue
    #이동 수행
    x,y = nx, ny
print(x,y)

