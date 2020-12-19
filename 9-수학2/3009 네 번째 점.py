x_arr = []
y_arr = []

tempX = 0
tempY = 0
for _ in range(0,3):
    a, b = map(int, input().split())
    x_arr.append(a)
    y_arr.append(b)

if x_arr[0] == x_arr[1]:
    tempX = x_arr[2]
elif x_arr[1] == x_arr[2]:
    tempX = x_arr[0]
else:
    tempX = x_arr[1]

if y_arr[0] == y_arr[1]:
    tempY = y_arr[2]
elif y_arr[1] == y_arr[2]:
    tempY = y_arr[0]
else:
    tempY = y_arr[1]

print(tempX, tempY)
