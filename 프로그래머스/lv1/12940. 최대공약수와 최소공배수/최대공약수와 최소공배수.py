def solution(n, m):
    answer = []
    result = 0
    #최대 공약수
    for i in range(1,min(n,m)+1):
        if n % i == 0 and m % i == 0:
            result = i
    answer.append(result)
    #최소 공배수 
    for i in range(n*m,max(n,m)-1,-1):
        if i % n == 0 and i % m ==0:
            result = i
    answer.append(result) 
    return answer