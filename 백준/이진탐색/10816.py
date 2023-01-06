from bisect import bisect_left, bisect_right
import sys

n = int(sys.stdin.readline())
a = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))


def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index


for i in b:
    result = count_by_range(a, i, i)
    print(result,end=' ')
