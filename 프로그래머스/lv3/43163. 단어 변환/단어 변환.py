from collections import deque

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    visited = [0 for i in range(len(words))]
    queue = deque()
    queue.append([begin,0])
    
    
    
    while queue:
        word, cnt = queue.popleft()
        if word == target:
            return cnt
        
        for i in range(len(words)):
            ck = 0
            if visited[i] == 0:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        ck+=1
                if ck ==1:
                    visited[i] = 1
                    queue.append([words[i],cnt+1])
    return 0