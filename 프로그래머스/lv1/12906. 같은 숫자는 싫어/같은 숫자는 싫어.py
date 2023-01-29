def solution(arr):
    result = []
    for i in arr:
        if i not in result:
            result.append(i)
        else:
            if result[len(result)-1] != i:
                result.append(i)
    return result