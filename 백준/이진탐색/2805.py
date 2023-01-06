import sys

n, m = map(int, sys.stdin.readline().split())  # 나무의수 n 상근이가 집으로 가져 가려고하는 나무의 길이 m
arr = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(arr)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in arr:
        if i >= mid:
            total += i - mid
    if total >= m:  # 오른쪽 탐색
        start = mid + 1
    else:
        end = mid - 1

print(end)
