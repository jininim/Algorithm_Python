n = int(input())
p = list(map(int,input().split()))
p.sort()
sum1 = 0
result = 0
for i in p:
    sum1 += i
    result += sum1
print(result)