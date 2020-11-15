import sys


def hansu(N):
    arr = list(range(1, N+1))
    count = 0
    for number in arr:
        if number < 100 or (int(str(number)[0]) - int(str(number)[1])) == (int(str(number)[1]) - int(str(number)[2])):
            count += 1
    print(count)


input_num = sys.stdin.readline

N = int(input_num())

hansu(N)
