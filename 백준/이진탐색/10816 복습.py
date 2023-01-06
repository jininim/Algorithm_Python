import sys
from bisect import bisect_left, bisect_right

n = sys.stdin.readline()
a = sorted(list(map(int, sys.stdin.readline().split())))

m = sys.stdin.readline()
b = list(map(int, sys.stdin.readline().split()))


# 데이터의 개수를 반환하는 함수
def count_by_range(a, value):
    right_index = bisect_right(a, value)
    left_index = bisect_left(a, value)
    return right_index - left_index


for i in b:
    print(count_by_range(a, i), end=" ")
