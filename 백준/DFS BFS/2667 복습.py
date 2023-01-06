# 지도의 크기
n = int(input())

for _ in range(n):
    graph = list(map(int, input()))

cnt = 0
result = 0
count = []


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    # 방문하지 않은 경우
    if graph[x][y] == 1:
        global cnt
        # 카운트 1 증가
        cnt += 1
        # 방문처리
        graph[x][y] = 0

        dfs(x - 1, y)  # 상
        dfs(x, y - 1)  # 좌
        dfs(x + 1, y)  # 하
        dfs(x, y + 1)  # 우
        return True
    return False


for i in range(n):
    for j in range(n):
        if dfs(i, j):
            result += 1
            count.append(cnt)
            cnt = 0

print(result)
count.sort()  # 오름차순으로 정렬
for i in count:
    print(i)
