def solution(s):
    arr = []
    if len(s) % 2 != 0:
        return 0
    else:
        if s:
            arr.append(s[0])
        for i in range(1,len(s)):
            if arr:
                if arr[-1] == s[i]:
                    arr.pop()
                else:
                    arr.append(s[i])
            else:
                arr.append(s[i])
        if arr:
            return 0
        else:
            return 1
        
