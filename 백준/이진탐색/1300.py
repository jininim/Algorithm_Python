n = int(input())  # 배열의 크기
k = int(input())


def bianry_search(target, start, end):
    while start <= end:
        # 중간값
        mid = (start + end) // 2

        # 내가 원하는 인덱스의 값
        cnt = 0
        for i in range(1, n + 1):
            cnt += min(mid // i, n)

        if cnt >= target:
            end = mid - 1
        else:
            start = mid + 1
    return start


print(bianry_search(k, 1, n * n))
