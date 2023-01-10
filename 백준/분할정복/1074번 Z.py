n, r, c = map(int, input().split())

while n != 0:
    n -= 1
    # 1사분면
    if r < 2 ** n and c < n:
        pass
    # 2사분면
    if r < 2 ** n <= c:
        pass
    # 3사분면
    if r >= 2 ** n > c:
        pass
    # 4사분면
    if r >= 2 ** n and c >= n:
        pass


