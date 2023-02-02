def solution(n, arr1, arr2):
    arrb1 = []
    arrb2 = []
    result = [[" "] * n for i in range(n) ]
    arr = []
    for i in arr1:
        if len(format(i,'b')) < n:
            arrb1.append("0"* (n-len(format(i,'b'))) + (format(i,'b')))
        else:
            arrb1.append(format(i,'b'))
    for i in arr2:
        if len(format(i,'b')) < n:
            arrb2.append("0"* (n-len(format(i,'b'))) + (format(i,'b')))
        else:
            arrb2.append(format(i,'b'))     
    for i in range(n):
        for j in range(n):
            if arrb1[i][j] == "1" or arrb2[i][j] == "1":
                result[i][j] = "#"
    for i in range(n):
        arr.append("".join(result[i]))
    return arr
    