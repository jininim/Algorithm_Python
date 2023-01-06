v = int(input())
# 100*100 배열 선언
arr = [[0] * 100 for _ in range(100)]
cnt = 0
for _ in range(v):
    a, b = map(int, input().split())
    # 색종이 크기가 도화지를 넘어 갈 경우
    if b + 10 >= 100 and a + 10 >= 100:
        for i in range(b, 100):
            for j in range(a, 100):
                arr[i][j] = 1

    else:
        for i in range(b, b + 10):
            for j in range(a, a + 10):
                arr[i][j] = 1

for i in range(100):
    cnt += arr[i].count(1)
print(cnt)
