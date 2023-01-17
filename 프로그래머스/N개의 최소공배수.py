arr = [2, 6, 8, 14]
# for i in range(max(n, m), n * m + 1):
#     if i % n == 0 and i % m == 0:
#         answer.append(i)
result = [1]
for i in arr:
    for j in range(max(result[0], i), result[0] * i + 1):
        if j % result[0] == 0 and j % i == 0:
            result[0] = j
            break
print(result[0])
