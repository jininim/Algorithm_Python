def solution(t, p):
    cnt = 0
    for i in range(len(t)-(len(p)-1)):
        _t = int(t[i:i+len(p)])
        if _t <= int(p):
            cnt +=1
    return cnt