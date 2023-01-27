def solution(x):
    x = str(x)
    sum = 0
    for i in x:
        sum = sum + int(i)
    if int(x) % sum == 0:
        return True
    else:
        return False