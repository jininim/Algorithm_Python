def solution(str1, str2):
    arr = []
    for i,j in zip(str1,str2):
        arr.append(i)
        arr.append(j)
    return ''.join(arr)