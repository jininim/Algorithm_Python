from collections import deque
def solution(s):
    if len(s) == 1:
        return 0
    s = list(s)
    a = deque(s)
    result = 0
    for i in range(len(s)):
        arr = []
        arr.append(a[0])
        if arr[0] == ']' or arr[0] == ')' or arr[0] == '}':
            a.rotate(1)
            continue
            
                 
        for j in range(1,len(a)):
            if arr:
                if arr[-1] == '[' and a[j] == ']' or arr[-1] == '(' and a[j] == ')' or arr[-1] == '{' and a[j] == '}':
                    arr.pop()
                else:
                    arr.append(a[j])
            else:
                arr.append(a[j])
        if not arr:
            result +=1
        a.rotate(1)
                           
    return result