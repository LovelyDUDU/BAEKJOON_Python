import sys

input_num = sys.stdin.readline

N = int(input_num())

for _ in range(N):
    count = 0  # 평균 넘는 사람
    arr = list(map(int, input_num().split()))
    avg = (sum(arr) - arr[0]) / arr[0]
    for i in range(1, len(arr)):
        if arr[i] > avg:
            count = count + 1
    print('%.3f' % (count / arr[0] * 100) + "%")
