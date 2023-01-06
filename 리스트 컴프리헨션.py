# 리스트 설명
a = [1,2,3,4,5,6,7]

# 리스트 슬라이싱 첫번째 인덱스 부터 마지막 인덱스-1까지
print(a[1:4])

# 리스트 컴프리헨션
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트.
array = [i for i in range(20) if i % 2 == 1]
# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array = [ i * i for i in range(1,10)]

# N X M 크기의 2차원 리스트 초기화 -> 반드시 리스트 컴프리헨션 이용
n = 3
m = 4
array = [[0] * m for _ in range(n)]

# remove_set에 포함되지 않은 값만을 저장
remove_set = {3,5}
result = [i for i in a if i not in remove_set]
print(array)
