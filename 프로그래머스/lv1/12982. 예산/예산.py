def solution(d, budget):
    d.sort()
    cnt = 0
    money = budget
    for i in d:
        if money - i >= 0:
            money -= i
            cnt +=1
    return cnt