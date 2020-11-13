import sys

input_num = sys.stdin.readline

N = int(input_num())
arr = list(map(int, input_num().split()))

max_num = max(arr)

for i in range(N):
    arr[i] = arr[i] / max_num * 100

print(sum(arr) / len(arr))

# n=int(input())
# arr = list(map(int,input().split()))
# M = max(arr)
# mean = sum(arr)/n
# print(mean/M*100)
# 다른 사람들꺼 보니깐 굳이 반복문으로 배열 안에 있는 값들에 일일이 연산해줄 필요가 없다.
# 그냥 평균값 낸 다음에 거기서 한번만 연산해도 됨....