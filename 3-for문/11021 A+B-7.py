import sys
input = sys.stdin.readline
x = int(input())
for i in range(1,x+1):
    a,b = map(int, input().split())
    print("Case #"+str(i)+":", a+b)


# T=int(input())
# for i in range(T):
#     a,b=map(int,input().split())
#     print('Case #{}: {}'.format(i+1, a+b))
# 이런식으로 format해서 할 수도 있다. java하다가 python으로 하려니 문법을 잘 모르겠다