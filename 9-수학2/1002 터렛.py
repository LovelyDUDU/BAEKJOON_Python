import math

T = int(input())


def position(x1, y1, r1, x2, y2, r2):
    i = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if x1 == x2 and y1 == y2:
        if r1 != r2:
            print(0)
        else:
            print(-1)
    elif r1+r2 < i or abs(r2-r1) > i: # 원의 접점이 없는경우
        print(0)
    elif abs(r2-r1) == i or r1+r2 == i: # 월의 점점이 하나인경우
        print(1)
    else: # 원의 접점이 2개인경우
        print(2)


for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    position(x1, y1, r1, x2, y2, r2)
