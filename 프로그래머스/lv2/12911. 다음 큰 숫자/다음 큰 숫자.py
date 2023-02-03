def solution(n):
    a = format(n,'b')
    a = str(a)
    b = n +1
    while True:
        c = format(b,'b')
        c = str(c)
        if a.count('1') == c.count('1'):
            break
        b += 1
    return b
        