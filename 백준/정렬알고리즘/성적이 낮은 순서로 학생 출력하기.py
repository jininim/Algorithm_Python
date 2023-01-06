import data as data

n = int(input())
array = []
for _ in range(n):
    input_data = input().split()
    array.append((input_data[0],int(input_data[1])))

# 키를 이용하여 점수를 기준으로 정렬
array = sorted(array, key= lambda data: data[1])

# 결과 출력
for i in array:
    print(i[0],end=" ")
