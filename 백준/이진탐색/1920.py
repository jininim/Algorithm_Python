import sys

n = sys.stdin.readline()
a = sorted(list(map(int, sys.stdin.readline().split())))

m = sys.stdin.readline()
b = list(map(int, sys.stdin.readline().split()))


def binary_search(arr, target, start, end):  # 이분 탐색 함수 정의
    if start > end:
        return 0
    mid = (start + end) // 2
    if arr[mid] == target:
        return 1
    # 중간값이 target보다 크다면
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)


for i in b:  # i를 b 리스트 값을 받아옴
    print(binary_search(a, i, 0, (len(a) - 1)))
