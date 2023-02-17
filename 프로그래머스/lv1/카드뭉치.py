from collections import deque
def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    q = deque(goal)
    while q:
        if cards1:
            x = cards1[0]
        if cards2:
            y = cards2[0]
        val = q.popleft()
        if val == x:
            cards1.popleft()
        elif val == y:
            cards2.popleft()
        else:
            return "No"
    return "Yes"