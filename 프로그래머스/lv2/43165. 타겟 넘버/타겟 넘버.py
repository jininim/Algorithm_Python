def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    def dfs(idx,total):
        nonlocal answer
        
        if idx ==n: # 모든 숫자를 다 확인하면
            if total == target:
                answer+=1
            return
        dfs(idx+1,total+numbers[idx])#현재 숫자를 더하는 경우
        dfs(idx+1,total-numbers[idx])#현재 숫자를 뺄경우
    dfs(0,0)
    return answer