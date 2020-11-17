N = int(input())

count = N

for _ in range(N):
    temp = []
    before = ""
    word = input()
    for w in word:
        if w not in temp:
            temp.append(w)
            before = w
        elif w in temp and before == w:
            temp.append(w)
        elif w in temp and before != w:
            count -= 1
            break

print(count)

# a = int(input())
# count = 0
#
# for i in range(a):
#     b = input()
#     print(sorted(b, key=b.find))
#     if list(b) == sorted(b, key=b.find):
#         count += 1
#
# print(count)

# 다른사람의 코드인데 find 부분에 대해 이해가 안가서 print로 찍어봤다.
# sort를 하는데 같은 문자끼리 묶는 것 같다.