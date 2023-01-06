n = int(input())
length = list(map(int, input().split()))
price = list(map(int,input().split()))
result = 0
a = price[0]

for i in range(n-1):
    if price[i] < a:
        a = price[i]
    result += a * length[i]

print(result)
#구글 참조.






