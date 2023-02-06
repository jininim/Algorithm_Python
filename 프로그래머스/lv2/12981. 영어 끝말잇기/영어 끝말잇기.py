def solution(n, words):
    arr = []
    result = []
    number = 0
    sum = 1
    for i in words:
        if arr:
            if i not in arr:
                if arr[-1][-1] == i[0]:
                    arr.append(i)
                    number +=1
                    if number == n+1:
                        number = 1
                        sum +=1
                else:
                    number +=1
                    if number == n+1:
                        number = 1
                        sum +=1
                    break
            else:
                number+=1
                if number == n+1:
                    number = 1
                    sum +=1
                break
        else:
            number+=1
            arr.append(i)
    if len(words) == len(arr):
        return [0,0]
    else:
        return [number,sum]
    
   

