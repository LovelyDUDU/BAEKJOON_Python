import math

M = int(input())
N = int(input())
total = 0
count = 0
min = 0


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
        if count == 0:
            min = M
            count += 1
        total += M
    M += 1
    if M > N:
        break

if total == 0:
    print(-1)
else:
    print(total)
    print(min)
