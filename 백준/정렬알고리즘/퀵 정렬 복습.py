array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    # 원소가 1개인 경우 종료
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    # 엇갈리지 않을 때 까지 반복
    while left <= right:

        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1

        # 엇갈렸다면
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    # 피벗 기준 왼쪽과 오른쪽 부분에서 퀵 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)