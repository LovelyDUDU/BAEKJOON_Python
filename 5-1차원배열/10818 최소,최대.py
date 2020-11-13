import sys
input_num = sys.stdin.readline
N = int(input_num())
arr = []
arr = input_num().split(' ')
new_arr = list(map(int,arr))
min = new_arr[0]
max = new_arr[0]
for i in range(len(arr)):
    if min > new_arr[i]:
        min = new_arr[i]
    if max < new_arr[i]:
        max = new_arr[i]

print(min,max)

# n = int(input())
# li = list(map(int, input().split()))
# 
# print(min(li), max(li))
# 아 파이썬 라이브러리 ㅋㅋㅋ min이랑 max가 있다는걸 깜빡했다.... 심지어 split도 그냥 () 하면 될것을 굳이 ' ' 넣었네