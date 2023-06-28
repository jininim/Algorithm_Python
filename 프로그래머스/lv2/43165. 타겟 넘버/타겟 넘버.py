from collections import deque
def solution(numbers, target):
    answer = 0
    n = len(numbers)
    q = deque()
    q.append([0,0])
    
    while q:
        idx,total = q.popleft()
        
        if idx == n:
            if total == target:
                answer+=1
            continue
        q.append([idx+1,total+numbers[idx]])
        q.append([idx+1,total-numbers[idx]])
    return answer