def solution(numbers):
    sum = 45
    for i in range(1,10):
        if i in numbers:
            sum -= i
    return sum