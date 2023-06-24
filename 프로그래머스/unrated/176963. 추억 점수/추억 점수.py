def solution(name, yearning, photo):
    answer = dict(zip(name,yearning))
    result = []
    for i in photo:
        sum = 0
        for j in i:
            sum += answer.get(j,0)
        result.append(sum)
    return result