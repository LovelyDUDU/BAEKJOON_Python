'''
A, B, V = list(map(int, input().split()))

tree = 0
day = 1
total = A - B
while True:
    tree = tree + total
    if tree >= V:
        print(day-1)
        break
    day += 1
'''
import math
A, B, V = list(map(int, input().split()))

print(math.ceil((V-B)/(A-B)))