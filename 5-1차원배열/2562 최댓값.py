import sys

input_num = sys.stdin.readline
max_num = 0
count = 0
for i in range(9):
    temp = int(input_num())
    if max_num < temp:
        max_num = temp
        count = i + 1

print(max_num)
print(count)

# new = [0]
# for _ in range(9):
#     n = int(input())
#     new.append(n)
# print(max(new))
# print(new.index((max(new))))

# 배열을 만들어놓고 max를 쓰는 방법도 있다. 그리고 index를 써서 배열의 몇번째에 있는지 확인
