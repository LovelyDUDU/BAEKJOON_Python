import sys

input_num = sys.stdin.readline

arr = []
count = 0
for _ in range(10):
    x = int(input_num()) % 42
    if x not in arr:
        count = count + 1
        arr.append(x)

print(count)

# ilist = []
#
# for n in range(10):
#   a = int(input())
#   ilist.append(a%42)
#
# ilist = set(ilist)
# print(len(ilist))

# set을 이용해서 중복을 제거하는 방법도있음...