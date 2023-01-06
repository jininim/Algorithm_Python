import sys

k, n = map(int, sys.stdin.readline().split())  # 랜선의 개수, 필요한 랜선의 개수
arr = []
for _ in range(k):  # 랜선의 길이 입력
    arr.append(int(sys.stdin.readline()))

# 이분 탐색 수행
start = 1
end = max(arr)
while start <= end:
    mid = (start + end) // 2  # 랜선을 자르려는 길이
    total = 0
    for x in range(k):
        total += arr[x] // mid  # 주어진 랜선의 길이를 자를경우 나오는 랜선의 개수를 저장
    if total >= n:  # 만들어진 랜선의 수가 필요한 랜선의 수 보다 적다면.
        start = mid + 1
    else:
        end = mid - 1

print(end) # 최대 길이를 찾아야 하므로 end 출력
