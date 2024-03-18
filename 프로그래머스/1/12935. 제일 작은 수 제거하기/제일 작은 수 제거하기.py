def solution(arr):
    del arr[arr.index(min(arr))]
    if arr:
        return arr
    else:
        arr.append(-1)
        return arr
    return answer