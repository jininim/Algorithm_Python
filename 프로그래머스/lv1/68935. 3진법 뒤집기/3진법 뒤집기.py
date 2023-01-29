def solution(num):
    cnt = 0
    arr = []
    n = 0
    sum = 0
    while True:
        if 3 ** n > num:
            cnt = n-1
            break
        n +=1
    for i in range(cnt,-1,-1):
        arr.append(num // 3**i)
        num = num % 3 ** i
    arr.reverse()
    cnt = 0
    for i in range(len(arr)-1,-1,-1):
        sum += arr[i] * (3**cnt)
        cnt +=1
    return sum