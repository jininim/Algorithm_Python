N, M, K = map(int, input().split())
a = list(map(int, input().split()))
result = 0
i = 0
a.sort()
while True:
    for i in range(K): # 가장 큰 수를 K번 더하기
        if M == 0: # m이 0이라면 반복문 탈출
            break
        result += a[N-1]
        M -= 1 # 더할 때마다 m 1씩 감소
    if M == 0:
        break
    result += a[N-2] # 두 번째로 큰 수를 한 번 더하기
    M -= 1


print(result)
