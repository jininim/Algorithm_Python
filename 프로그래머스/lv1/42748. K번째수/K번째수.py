def solution(arr, commands):
    result = []
    k= []
    answer = []
    for i in commands:
        result.append(arr[i[0]-1:i[1]])
        k.append(i[2]-1)
    for i in result:
        i.sort()
    for i in range(len(result)):
        answer.append(result[i][k[i]])
    return answer