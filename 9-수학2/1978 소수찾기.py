import math

N = input()
arr = list(map(int, input().split()))
count = 0


def sosu(num):
    if num < 2:
        return False
    start = 2
    point = int(math.sqrt(float(i)))
    if start > point:
        return True
    for _ in range(point):
        if num % start == 0:
            return False
        else:
            start += 1
    return True


for i in arr:  # 하나씩 뺴서 확인해야함
    if sosu(i):
        count += 1

print(count)
