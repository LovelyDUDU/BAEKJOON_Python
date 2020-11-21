T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    under_floor = []

    for i in range(n):
        under_floor.append(i + 1)

    for _ in range(k):
        temp_floor = under_floor
        for i in range(n):
            if i == 0:
                under_floor[i] == 0
            else:
                under_floor[i] = temp_floor[i] + under_floor[i - 1]

    print(under_floor[n - 1])


#  생각보다 금방 풀었다. 내 꿈은 오늘부터 부녀회장이다......