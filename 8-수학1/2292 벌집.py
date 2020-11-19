'''
1   6       12      18      24      ...
1   2~7     8~19    20~37   38~61   ...
'''
N = int(input())

max = 1
count = 1
while True:
    if max < N:
        max = max + 6 * count
        count += 1
    else:
        print(count)
        break