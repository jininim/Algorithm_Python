def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    scores = [0, 0, 0]  # 각 수포자의 점수를 저장할 리스트

    # 정답과 수포자의 패턴을 비교하여 점수를 계산
    for i in range(len(answers)):
        for j in range(3):
            if answers[i] == patterns[j][i % len(patterns[j])]:
                scores[j] += 1
    max_scores = max(scores)
    answer = []
    for i in range(len(scores)):
        if scores[i] == max_scores:
            answer.append(i+1)
            
    return answer