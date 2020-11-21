import math

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    distance = y - x
    count = 1

    N = int(math.sqrt(distance))  # 거리 distance의 제곱근
    M = N + 1

    if N == 1:  # 거리차이가 1,2,3 인경우
        print(distance)
    elif distance >= N * M + 1:
        print(N + M)
    elif distance >= N ** 2 + 1:
        print(N * 2)
    else:  # 4인경우
        print(N * 2 - 1)

