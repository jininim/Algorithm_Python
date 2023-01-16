def fibo(n):
    arr = [0] * (n+1)
    arr[1] = 1
    arr[2] = 1
    for i in range(3, n + 1):
        arr[i] = arr[i - 2] + arr[i - 1]
    return arr[n] % 1234567


print(fibo(5))
