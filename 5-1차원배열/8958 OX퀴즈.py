import sys

input_ox = sys.stdin.readline

N = int(input_ox())
new_arr = []

for _ in range(N):
    arr = list(input_ox())
    score = 0
    count = 1
    for i in range(len(arr)):
        if arr[i] == "O":
            score = score + count
            count = count + 1
        else:
            count = 1
    print(score)

