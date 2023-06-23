def solution(numbers):
    # 숫자를 문자열로 변환합니다.
    numbers = list(map(str, numbers))

    numbers.sort(key=lambda x: x*3, reverse=True)

    answer = ''.join(numbers)

    if answer[0] == '0':
        answer = '0'

    return answer