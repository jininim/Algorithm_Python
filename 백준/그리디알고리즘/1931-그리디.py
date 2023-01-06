n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))  # 리스트안에 리스트 입력받기
a = sorted(a, key=lambda a: a[0])  # 시작 시간을 기준으로 정렬
a = sorted(a, key=lambda a: a[1])  # 끝나는 시간을 기준으로 정렬.
cnt = 0
end = 0
for i, j in a:
    if i >= end:  # 시작시간이 끝나는 시간보다 크거나 같으면
        cnt += 1  # 작업을 하나 증가
        end = j
print(cnt)
