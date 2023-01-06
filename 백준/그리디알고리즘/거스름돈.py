n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인하기
array = [500, 100, 50, 10]

for coin in array:
    count += n // coin  # count에 n을 coin으로 나눈 몫을 저장
    n %= coin  # n에 n을 coin으로 나눈 나머지값을 저장
print(count)
