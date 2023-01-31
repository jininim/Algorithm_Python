def solution(sizes):
    arr_w = []
    arr_h = []
    for i in sizes:
        i.sort()
        arr_w.append(i[0])
        arr_h.append(i[1])
    return max(arr_w)*max(arr_h)
 