import sys

n = int(input())
count = []
new_list = []
for _ in range(n):  # 입력
    a = sys.stdin.readline().strip()
    count.append(a)

for value in count:
    if value not in new_list:
        new_list.append(value)


new_list.sort()
new_list.sort(key=len)

for j in new_list:
    print(j)
