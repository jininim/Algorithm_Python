n, m = map(int, input().split())

a = []
b = []
c = [[] * m for i in range(n)]
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    b.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        x = a[i][j] + b[i][j]
        c[i].append(x)

for i in range(n):
    print(*c[i])
