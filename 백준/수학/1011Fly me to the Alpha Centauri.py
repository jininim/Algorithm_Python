t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    z = y - x
    result = 0
    if z <= 3:
        print(z)
    elif z<=8:
        #이동거리가 홀수 일 경우
        if z % 2 == 1:
            result = 3 + (z-3)//2
            print(result)
        else:
            result = 2 + (z-2)//2
            print(result)

    # 이동거리
    # 1 2 3 4 5 6 7 8
    # 횟수
    # 1 1+1 1+1+1 1+2+1 1+2+1+1 1+2+2+1 1+2+2+1+1 1+2+2+2+1 1+2+3+2+1 1+2+3+2+1+1 1+2+3+2+2+1
        