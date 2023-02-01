def solution(arr):
    cnt = 0
    for i in range(len(arr)-2):
        for j in range(i+1,len(arr)-1):
            for k in range(j+1,len(arr)):
                sum = arr[i] + arr[j] + arr[k]
                if sum == 0:
                    cnt+=1
    return cnt