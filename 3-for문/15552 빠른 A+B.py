# sys.stdin.readline을 쓰는 경우가 몇몇 보이길래 찾아봤다.
# input() 보다는 sys.stdin.readline이 시간단축에 도움이 된다고 한다.

# 입출력 속도 비교 : sys.stdin.readline() > raw_input() > input()
# sys.stdin.readline를 쓰도록 해야겠다.
# input = sys.stdin.readline 라고 상단에 정의하고 쓰면 될것같다.

import sys
input = sys.stdin.readline
x = int(input())
for i in range(0,x):
    a,b = map(int,input().split())
    print(a+b)