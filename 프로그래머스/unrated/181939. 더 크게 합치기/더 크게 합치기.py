def solution(a, b):
    summ =  str(a) + str(b)
    reversSum = str(b) + str(a)
    if int(summ) >= int(reversSum):
        return int(summ)
    else:
        return int(reversSum)
