import sys

n, m = map(int, sys.stdin.readline().split())
arr1 = set()  # 듣도 못한 사람 집합
arr2 = set()  # 보도 못한 사람 집합

# 듣고 못한 사람 입력
for _ in range(n):
    arr1.add(sys.stdin.readline().rstrip())
# 보도 못한 사람 입력
for _ in range(m):
    arr2.add(sys.stdin.readline().rstrip())
# set 자료구조를 사용하여 arr1 과 arr2의 교집합을 리스트로 변환하여 result 리스트를 만듬
result = list(arr1 & arr2)
result.sort()
# 결과출력
print(len(result))
for i in result:
    print(i)
