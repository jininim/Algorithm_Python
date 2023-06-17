def solution(n, lost, reserve):
    answer = n - len(lost)
    lost.sort()
    reserve.sort()

    # 여벌 체육복을 가져온 학생이 도난당한 경우 처리
    for i in lost[:]:
        if i in reserve:
            answer += 1
            lost.remove(i)
            reserve.remove(i)

    # 체육복 빌려주기
    for i in reserve:
        if i-1 in lost:
            answer += 1
            lost.remove(i-1)
        elif i+1 in lost:
            answer += 1
            lost.remove(i+1)

    return answer