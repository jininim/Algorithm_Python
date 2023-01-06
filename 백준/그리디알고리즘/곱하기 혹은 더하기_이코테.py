S = input()
value = 0

for i in S:
    j = int(i)
    if j <= 1:  # 값이 1이하인 경우는 더해준다
        value += j
    elif j != 0:  # value의 값이 0인 경우를 제외하고는 값을 value와 곱해준다.
        if value == 0:
            value = 1
        value *= j

print(value)
