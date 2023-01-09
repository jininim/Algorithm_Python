import sys

t = int(sys.stdin.readline())
for _ in range(t):
    a = int(sys.stdin.readline())
    if a == 0:
        print(1, 0)
        continue
    elif a == 1:
        print(0, 1)
        continue
    arr = [[0] * 2 for _ in range(a + 1)]
    arr[0] = [1, 0]
    arr[1] = [0, 1]
    for i in range(2, a + 1):
        arr[i] = [arr[i - 2][0] + arr[i - 1][0], arr[i - 2][1] + arr[i - 1][1]]
    print(arr[a][0], arr[a][1])
