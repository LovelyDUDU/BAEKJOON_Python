import math

M, N = map(int, input().split())


def sosu(num):
    if num < 2:
        return False
    start = 2
    point = int(math.sqrt(float(num)))
    if start > point:
        return True
    for _ in range(point):
        if num % start == 0:
            return False
        else:
            start += 1
    return True


while True:
    if sosu(M):
        print(M)
    M += 1
    if M > N:
        break
