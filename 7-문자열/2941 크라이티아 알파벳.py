eng = input()

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for x in cro:
    eng = eng.replace(x, '@')
print(len(eng))

# eng = input()
#
# arr = list(eng)
#
# count = 0
# i = 0
#
# while True:
#     if len(arr) <= i:
#         break
#     if arr[i] == "c" and (arr[i+1] == "=" or arr[i+1] == "-"):
#         count += 1
#         i += 2
#     elif arr[i] == "d" and (arr[i+1] == "-"):
#         count += 1
#         i += 2
#     elif arr[i] == "d" and arr[i+1] == "z" and arr[i+2] == "=":
#         count += 1
#         i += 3
#     elif (arr[i] == "l" or arr[i] == "n") and arr[i+1] == "j":
#         count += 1
#         i += 2
#     elif (arr[i] == "s" or arr[i] == "z") and arr[i+1] == "=":
#         count += 1
#         i += 2
#     else:
#         count += 1
#         i += 1
#
#
# print(count)
#
# test case는 문제 없는데 런타임 오류란다 ㅠㅠㅠ 왜지??ㅠㅠㅠㅠㅠ
