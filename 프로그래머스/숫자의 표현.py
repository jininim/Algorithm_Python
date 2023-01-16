n = 7
cnt = 0
for i in range(1, n + 1):
    result = i
    j = i + 1
    while result <= n:
        if result == n:
            cnt += 1
            break
        result += j
        j += 1

print(cnt)
