array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):  # 첫 번째 원소는 이미 정렬된 상태로 2번째 원소부터 시작
    for j in range(i, 0, -1):  # 인덱스 i부터 1까지 감소하며 반복되는 문법
        if array[j] < array[j - 1]:  # 왼쪽에 숫자가 자기 보다 작다면 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else:  # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
print(array)
