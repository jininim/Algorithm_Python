import sys

n = int(input())
arr = []
for _ in range(n):
    a = sys.stdin.readline().split() # 입력
    arr.append((int(a[0]), a[1]))
arr_sort = sorted(arr,key=lambda data:data[0]) # 0번 인덱스 데이터로 정렬
for i in arr_sort: # 출력
    print(i[0],i[1])