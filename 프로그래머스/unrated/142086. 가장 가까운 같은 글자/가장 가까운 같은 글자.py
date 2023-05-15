def solution(s):
    answer = [-1]
    for i in range(1, len(s)):
        if s[i-1::-1].find(s[i]) != -1:
            answer.append(s[i-1::-1].find(s[i]) + 1)
        else:
            answer.append(-1)
        
    return answer