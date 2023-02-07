def solution(k, tangerine):
    arr = []
    tangerine.sort()
    cnt = 1
    result = 0
    for i in range(len(tangerine)):
        if i == len(tangerine)-1:
            arr.append([tangerine[i],cnt])
        elif tangerine[i] == tangerine[i+1]:
            cnt+=1
        else:
            arr.append([tangerine[i],cnt])
            cnt = 1
    arr.sort(key = lambda x:-x[1])
    
    for i in arr:
        k = k - i[1]
        result +=1
        if k <= 0:
            break
    return result
            
