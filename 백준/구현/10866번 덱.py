from collections import deque
import sys
n = int(sys.stdin.readline())
q = deque()

for _ in range(n):
    order = sys.stdin.readline()
    a = order.split()
    if a[0] == "push_back":
        q.append(a[1])
    elif a[0] == "push_front":
        q.appendleft(a[1])
    elif a[0] == "pop_front":
        if q:
            x = q.popleft()
            print(x)
        else:
            print(-1)
    elif a[0] == "pop_back":
        if q:
            x = q.pop()
            print(x)
        else:
            print(-1)
    elif a[0] == "size":
        print(len(q))
    elif a[0] == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif a[0] == "front":
        if q:
            x = q.popleft()
            q.appendleft(x)
            print(x)
        else:
            print(-1)

    elif a[0] == "back":
        if q:
            x = q.pop()
            q.append(x)
            print(x)
        else:
            print(-1)
