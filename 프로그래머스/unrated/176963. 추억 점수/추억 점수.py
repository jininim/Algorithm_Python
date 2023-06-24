def solution(name, yearning, photo):
    answer = {}
    result = []
    for i in range(len(name)):
        answer[name[i]] = yearning[i]
    for i in photo:
        sum = 0
        for j in i:
            sum += answer.get(j,0)
        result.append(sum)
    return result