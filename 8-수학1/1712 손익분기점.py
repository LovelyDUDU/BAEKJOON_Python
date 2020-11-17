numbers = list(map(int, input().split()))
if numbers[1] < numbers[2]:
    print(int(numbers[0] // (numbers[2] - numbers[1])) + 1)
else:
    print(-1)


# numbers = list(map(int, input().split()))
# point = int(numbers[0] // (numbers[2] - numbers[1])) + 1
# if numbers[1] >= numbers[2]:
#     point = -1
# print(point)

# 위에꺼는 되고 아래꺼는 안된다.... 왜지??????????