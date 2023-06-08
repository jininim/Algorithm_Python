from itertools import combinations
def is_prime(num):
    # 주어진 숫자가 소수인지 확인하는 함수
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    # nums에서 가능한 모든 3개의 숫자 조합을 생성
    combinations_list = combinations(nums, 3)
    
    for combination in combinations_list:
        # 조합의 합이 소수인지 확인
        if is_prime(sum(combination)):
            answer += 1
    
    return answer