from bisect import bisect_left, bisect_right


def count_by_range(a, value):
    right_index = bisect_right(a, value)
    left_index = bisect_left(a, value)
    return right_index - left_index


n = int(input())  # 상근이가 가진 숫자 카드
arr = list(map(int, input().split()))
m = int(input())
arr1 = list(map(int, input().split()))  # 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수
arr.sort()

for i in arr1:
    if count_by_range(arr,i):
        print(1,end=" ")
    else:
        print(0,end=" ")


