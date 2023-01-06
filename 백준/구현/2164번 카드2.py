from collections import deque

n = int(input())
q = deque()
x = 0

# 1~n 까지 숫자 입력
for i in range(1, n + 1):
    q.append(i)

while True:
    # q가 1이 될 때까지 반복문을 실행하며 마지막 남은 요소를 출력한다.
    if len(q) == 1:
        print(q.popleft())
        break
    q.popleft() # 카드 맨 윗장 버리기
    # 카드 맨 윗장을 뒤로 옮기기
    x = q.popleft()
    q.append(x)


