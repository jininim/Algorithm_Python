import sys
from collections import Counter

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()
print(round(sum(arr)/n)) # 산술평균
print(arr[len(arr) // 2]) # 중앙값
# 최빈값 contert 모듈 사용
counter = Counter(arr).most_common(2) # 가장 빈도수가 높은 2개 counter 변수에 받음
if len(counter) > 1: # 입력이 두개 이상인경우
    if counter[0][1] == counter[1][1]:  # 빈도수가 같으면
        print(counter[1][0]) # 두번째 숫자 출력
    else: # 같지 않으면
        print(counter[0][0])  # 첫번째 숫자 출력
else:
    print(counter[0][0]) # 입력이 하나면 첫번째 출력
print(max(arr)-min(arr)) # 범위

