import math, sys

input_num = sys.stdin.readline
count = 0


def sosu(num):
    arr = [True] * num
    n = int(num ** 0.5)
    for i in range(2, n + 1):
        if arr[i] == True:
            for j in range(i + i, num, i):
                arr[j] = False
    cnt = []
    for i in range(2, num):
        if arr[i] == True and i > num / 2:
            cnt.append(i)
    print(len(cnt))


while True:
    test = int(input_num())
    if test == 0:
        break
    if test == 1:
        print(1)
    else:
        sosu(test * 2)
