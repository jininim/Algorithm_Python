from collections import Counter

def solution(N, stages):
    counter = Counter(stages) #스테이지 별 도전자 수
    total_users = len(stages) # 전체 도전자 수
    failure_rates = [] # 실패율    

    for stage in range(1,N+1):
        users_on_stage = counter[stage] # 해당 스테이지 도전중인 사용자 수
        if total_users == 0:
            failure_rate = 0
        else:
            failure_rate = users_on_stage / total_users
        failure_rates.append((stage,failure_rate))
        total_users -= users_on_stage
    
    failure_rates.sort(key= lambda x: (-x[1],x[0]))  
    return [i[0] for i in failure_rates ]