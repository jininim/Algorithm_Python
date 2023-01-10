import sys

x = int(sys.stdin.readline())

# dp 테이블
d = [0 for _ in range(x+1)]

for i in range(2, x+1):
    # 1을 빼는경우
    d[i] = d[i - 1] + 1
    # 1을 뺄때와 3과 2로 나눌때 횟의 최솟값을 d[i]에 담는다
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
#결과 출력
print(d[x])
