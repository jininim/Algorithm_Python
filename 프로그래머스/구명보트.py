from collections import deque


def solution(arr, limit):
    cnt = 0
    arr = deque(sorted(arr))

    while len(arr) > 1:
        if arr[0] + arr[-1] <= limit:
            cnt += 1
            arr.pop()
            arr.popleft()
        else:
            cnt += 1
            arr.pop()
    if len(arr) == 1:
        cnt += 1

    return cnt
