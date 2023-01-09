import sys

k = int(sys.stdin.readline())
arr = []
for _ in range(k):
    a = int(sys.stdin.readline())
    if a != 0:
        arr.append(a)
    else:
        arr.pop()
print(sum(arr))
