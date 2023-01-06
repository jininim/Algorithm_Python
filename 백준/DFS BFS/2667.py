n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
result = 0 # 단지 수
cnt = 0 # 단지에 속하는 집의 수
count = [] # cnt 를 따로 담아줄 리스트


# DFS 깊이 우선 탐색을 통해 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):  # dfs 함수 정의

    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if graph[x][y] == 1: # 리스트의 값이 1인경우 - > 방문하지 않은경우
        global cnt
        cnt += 1 # 단지에 속하는 집의 수를 1증가

        graph[x][y] = 0 # 방문 표시

        dfs(x - 1, y)  # 상
        dfs(x, y - 1)  # 좌
        dfs(x + 1, y)  # 하
        dfs(x, y + 1)  # 우
        return True
    return False


for i in range(n):
    for j in range(n):
        if dfs(i, j): # dfs가 True인 경우
            result += 1 # 단지수 1 증가
            count.append(cnt) # 각 단지에 속한 집의 수를 각각 conut 리스트에 담아줌
            cnt = 0 # cnt 초기화

print(result)
count.sort() # 오름차순으로 정렬
for i in count:
    print(i)
