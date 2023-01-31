def solution(s, n):
    arr = []
    for i in s:
        if i.isupper():
            a = ord(i)
            if a+n > 90:
                a = a-26
            arr.append(chr(a+n))
        elif i.islower():
            a = ord(i)
            if a+n > 122:
                 a = a-26
            arr.append(chr(a+n))
        else:
            arr.append(" ")
    return ''.join(arr)