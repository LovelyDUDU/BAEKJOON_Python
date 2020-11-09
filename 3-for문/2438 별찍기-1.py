import sys
input = sys.stdin.readline
x = int(input())
for i in range(0,x):
    for j in range(0,i+1):
        print("*", end='')
    print("",end="\n")

# a=int(input())
# for i in range(1,a+1):
#     print(i*"*")

# 파이썬은 print안에 변수를 넣어서 반복도 가능하다. 