from collections import deque

def solution(k, m, score):
    answer = 0
    score.sort()
    deque_score = deque(score)
    arr= []
    while len(deque_score) >= m:
        for i in range(m):
                arr.append(deque_score.pop())
        answer += min(arr) * m
        arr.clear()
    
    return answer