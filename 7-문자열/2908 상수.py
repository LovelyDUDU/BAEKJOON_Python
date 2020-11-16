number = input()
arr = list(map(str, number.split()))

print(arr[0][::-1] if arr[0][::-1] > arr[1][::-1] else arr[1][::-1])

# A, B = input().split()
# a = A[::-1]
# b = B[::-1]
# print(max(int(a), int(b)))
#  이렇게 단순한 방법이?!ㅋㅋㅋㅋㅋㅋㅋ