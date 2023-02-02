def solution(arr):
    answer = set()
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            answer.add(arr[i]+arr[j])
    answer = list(answer)
    answer.sort()
    return answer