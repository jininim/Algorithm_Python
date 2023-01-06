from collections import deque

n, k = map(int, input().split())
q = deque()
arr = []
for i in range(1, n + 1):
    q.append(i)
# q가 비어있지 않은경우 실행
while q:
    # k-1 번 만큼 앞에 숫자를 뒤로 보내줌
    for _ in range(k - 1):
        x = q.popleft()
        q.append(x)
    arr.append(q.popleft())

# 정답 출력
print("<", end="")
for i in range(n):
    if i == n - 1:
        print(arr[i], end=">")
        break
    print(arr[i], end=", ")
