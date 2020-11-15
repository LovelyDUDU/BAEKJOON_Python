# N = int(input())
# for _ in range(N):
#     arr = list(input().split())
#     word = list(arr[1])
#     for w in word:
#         print(w * int(arr[0]), end='')
#     print()

N = int(input())
result = []
for _ in range(N):
    arr = list(input().split())
    word = list(arr[1])
    strs = ""
    for w in word:
        strs = strs + (w * int(arr[0]))
    result.append(strs)

for w in result:
    print(w)


# 처음에 제대로 했는데 마지막에 \n이 없어서 실패했었나보다...