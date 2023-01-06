# N,K를 공백을 기준으로 구분하여 입력 받기
N, K = map(int, input().split())
count = 0
# N이 1이 될 때 까지 반복문 실행
while N != 1:
    # N이 K로 나누어 떨어지면 아래 조건문 실행
    if N % K == 0:
        N = N // K
        count += 1
    else:
        N = N - 1
        count += 1

print(count)
