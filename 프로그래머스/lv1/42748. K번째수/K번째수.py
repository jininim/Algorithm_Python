def solution(arr, commands):
    result = []
    answer = []
    for i in commands:
        N_arr= (arr[i[0]-1:i[1]])
        N_arr.sort()
        answer.append(N_arr[i[2]-1])
    return answer