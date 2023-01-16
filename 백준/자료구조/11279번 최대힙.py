import sys
import heapq

maxheap = []
result = []
n = int(sys.stdin.readline())
for _ in range(n):
    a = int(sys.stdin.readline())
    if a > 0:
        # 최대힙 만드는 법
        heapq.heappush(maxheap, (-a, a))
    else:
        if len(maxheap) != 0:
            result.append(heapq.heappop(maxheap)[1])
        else:
            result.append(0)
for i in result:
    print(i)
