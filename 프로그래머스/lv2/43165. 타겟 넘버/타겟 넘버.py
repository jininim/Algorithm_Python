from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque([(0,0)])
    n = len(numbers)
    
    while queue:
        idx, total = queue.popleft()
        if idx ==n:
            if total == target:
                answer+=1
            continue
        queue.append((idx+1,total+numbers[idx]))
        queue.append((idx+1,total-numbers[idx]))
    return answer