def solution(n):
    result = 0
    val = n 
    while val > 0:
        if val % 2 == 0:
            val = val // 2
        else:
            val = val -1
            result +=1

    return result