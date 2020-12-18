import sys
from itertools import product

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
        if arr[i] == True:
            cnt.append(i)
    total = list(product(cnt, repeat=2))
    for i, j in total:
        if i > num/2:
            break
        if i+j == num:
            result = str(i) + " " + str(j)

    print(result)


test = int(input_num())
for _ in range(test):
    num = int(input_num())
    sosu(num)