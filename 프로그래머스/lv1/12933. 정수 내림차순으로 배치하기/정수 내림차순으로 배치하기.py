def solution(n):
    n = str(n)
    n = list(map(int,n))
    n.sort(reverse=True)
    return int(''.join(str(i) for i in n))