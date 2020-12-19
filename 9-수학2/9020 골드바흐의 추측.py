import sys

input_num = sys.stdin.readline

arr = [True] * 10002
for i in range(2, 10002):
    if arr[i] == True:
        for j in range(i + i, 10002, i):
            arr[j] = False

test = int(input_num())
for _ in range(test):
    num = int(input_num())
    fisrt_num = num//2
    second_num = fisrt_num

    while fisrt_num >0:
        if arr[fisrt_num]==True and arr[second_num] == True:
            print(fisrt_num, second_num)
            break
        else:
            fisrt_num-=1
            second_num+=1
