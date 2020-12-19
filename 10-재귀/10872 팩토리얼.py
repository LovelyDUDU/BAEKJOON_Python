def factorial(num):
    if num == 1:
        return num
    return num * factorial(num - 1)


N = int(input())
if N == 0 or N == 1:
    print(1)
else:
    print(factorial(N))
