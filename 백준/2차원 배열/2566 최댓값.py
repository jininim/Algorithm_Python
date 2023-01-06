a = []
ma = 0
de = 0
b = 0
for i in range(9):
    a.append(list(map(int, input().split())))

for i in range(9):
    if ma < max(a[i]):
        ma = max(a[i]) # 최댓값
        de = a[i].index(ma)  # 열 인덱스
        b = i  # 행 인덱스

print(ma)
print(b + 1, de + 1)
