import math
import sys

a, b, v = map(int, sys.stdin.readline().split())
result = (v - b) / (a - b)
print(math.ceil(result))
