'''
2
6 12 10
30 50 72

402
1203
'''

N = int(input())
for _ in range(N):
    arr = list(map(int, input().split()))

    floor = arr[2] % arr[0]
    if floor == 0:
        floor = arr[0]
    num = arr[2] // arr[0] + 1
    if arr[2] % arr[0] == 0:
        num -= 1
    room_num = floor * 100 + num
    print(room_num)

'''
t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    y = (n - 1) % h + 1
    x = (n - 1) // h + 1
    print("%d%02d" % (y, x))
'''