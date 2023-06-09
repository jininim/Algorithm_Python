def solution(lottos, win_nums):
    plus = lottos.count(0)
    cnt = 0
    answer = []
    for i in lottos:
        if i in win_nums:
            cnt +=1
    if cnt+plus != 0:
        answer.append(7-(plus+cnt))
    else:
        answer.append(6)
    if cnt < 2:
        answer.append(6)
    else:
        answer.append(7-cnt)
    
    return answer