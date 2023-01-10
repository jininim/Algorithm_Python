N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
result = []


def div(x, y, N):
    color = arr[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != arr[i][j]:
                # 제 1 사분면
                div(x, y, N // 2)
                # 제 2 사분면
                div(x, y + N // 2, N // 2)
                # 제 3 사분면
                div(x + N // 2, y, N // 2)
                # 제 4 사분면
                div(x + N // 2, y + N // 2, N // 2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)


div(0, 0, N)
print(result.count(0))
print(result.count(1))
