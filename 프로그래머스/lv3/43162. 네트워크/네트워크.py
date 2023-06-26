def solution(n, computers):
    answer = 0 # 네트워크의 개수
    
    #방문 여부
    visited = [False] * n
    
    def dfs(node):
        visited[node] = True # 현재 노드 방문처리
        
        #현재 노드와 연결된 다른 노드 탐색
        for i in range(n):
            #연결 되어있고 방문하지 않았다면,
            if computers[node][i] ==1 and not visited[i]:
                dfs(i)
                
    for i in range(n):
        # 방문하지 않은 노드 탐색
        if not visited[i]:
            dfs(i)
            answer += 1 # 네트워크 개수 증가
            
    return answer