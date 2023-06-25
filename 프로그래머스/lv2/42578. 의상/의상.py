
def solution(clothes):
    clothes_count = {}
    answer = 1
    
    
    for i in clothes:
        cloth_type = i[1] # 의상 종류
        if cloth_type in clothes_count:
            clothes_count[cloth_type] +=1
        else:
            clothes_count[cloth_type] = 1
    for i in clothes_count.values():
        answer *= (i+1)
    return answer-1