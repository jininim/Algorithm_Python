import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    # q = 중요도
    q = (list(map(int, sys.stdin.readline().split())))
    # arr = 순서
    arr = list(range(len(q)))
    # 내가 원하는 순서
    arr[m] = "target"

    cnt = 0

    while True:
        # 중요도가 가장 높으면
        if q[0] == max(q):
            # 출력순서 = cnt
            cnt += 1
            # 중요도가 가장 높고 원하는 순서이면 cnt 출력 while문 종료
            if arr[0] == "target":
                print(cnt)
                break
            # 원하는 순서가 아니면 리스트에서 삭제(프린터 출력)
            else:
                del q[0]
                del arr[0]
        # 중요도가 가장 높지 않으면
        else:
            # 출력 순서를 뒤로 배치
            q.append(q[0])
            del q[0]
            arr.append(arr[0])
            del arr[0]
