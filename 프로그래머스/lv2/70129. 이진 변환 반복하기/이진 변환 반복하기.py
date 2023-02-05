def solution(s):
    sum = 0
    i = 0
    while True:
        i +=1
        sum = sum + len(s) 
        s = s.replace("0","")
        sum = sum - len(s)
        s = (format(len(s),'b'))
        if len(s) == 1:
            break
    answer = []
    answer.append(i)
    answer.append(sum)
    return answer