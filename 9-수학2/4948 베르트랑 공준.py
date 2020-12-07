import math

count = 0


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
    test = int(input())
    if test == 0:
        break

    end = test * 2
    count = 0
    test += 1
    for _ in range(test, end+1):
        if sosu(test):
            count += 1
        test += 1
    print(count)

