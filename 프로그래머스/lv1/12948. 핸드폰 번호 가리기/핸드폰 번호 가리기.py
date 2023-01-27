def solution(p):
    arr = list(p)
    for i in range((len(arr)-4)):
        arr[i] = "*"
    answer = ''.join(arr)
    return answer