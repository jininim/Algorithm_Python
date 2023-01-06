# eval 함수 사용. 문자열 수식을 계산
# lstrip 함수  문자열 앞쪽 0들을 제거.
# a = input().split("-")
# result = 0
# for i in a[0].split("+"):
# for i in range(1, len(a)):
#     result = result - eval(a[i].lstrip("0"))
# print(result)
a = input().split("-")
result = 0
for i in a[0].split('+'):
    result += int(i)
for i in a[1:]:
    for j in i.split("+"):
        result -= int(j)
print(result)


