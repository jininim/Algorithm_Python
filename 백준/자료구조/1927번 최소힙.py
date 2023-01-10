import sys
import heapq

n = int(sys.stdin.readline())
heap = []
result = []
for _ in range(n):
    a = int(sys.stdin.readline())
    if a > 0:
        heapq.heappush(heap, a)
    else:
        if len(heap) != 0:
            result.append(heapq.heappop(heap))
        else:
            result.append(0)
for i in result:
    print(i)
