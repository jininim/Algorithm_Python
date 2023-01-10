import sys

n = int(sys.stdin.readline())

arr = list(map(int, input().split()))

# dp 테이블 초기화
d = [0] * n

# dp 진행 바텀업방식
d[0] = arr[0]
d[1] = max(arr[0], arr[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + arr[i])
print(d[n - 1])
