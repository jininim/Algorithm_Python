s = int(input())
result = 0
value = 1
n = 0
while result < s:
    result += value
    value += 1
    n += 1
    if result == s:
        break
    if result > s:
        result = result - value
        n -= 1
        a = value
        value = s - result
        while value < a:
            result = result - (a - 1)
            value = s - result
            n -= 1
        result += value
        n += 1
print(n)
