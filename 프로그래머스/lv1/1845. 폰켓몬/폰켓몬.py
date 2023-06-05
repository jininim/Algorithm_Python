def solution(nums):
    length = len(nums) / 2
    check = []
    for i in nums:
        if i not in check:
            check.append(i)
    answer = len(check)
    if answer > length:
        return length
    else:
        return answer