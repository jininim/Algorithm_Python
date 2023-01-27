def solution(s):
    a = len(s)/2
    if int(a) != len(s)/2:
        return s[int(a+1)-1]
    else:
        return s[int(a)-1:int(a)+1]
    