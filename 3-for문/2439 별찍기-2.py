import sys
input = sys.stdin.readline
x = int(input())

for i in range(1,x+1):
    print((x-i) * " ", end="")
    print(i*"*")


# n=int(input())
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*i)

# 이렇게 한줄에 여러개도 출력 가능하다!

# N=int(input())
# for i in range(1,N+1):
#     print(str("*"*i).rjust(N))

# 이런식으로 rjust를 이용해서 공백을 특정 문자로 채울 수도 있다.

# zfill(width) 사용법
# 입력 : "2".zfill(3)
# 출력 : 002

# rjust(width, [fillchar]) 사용법
# 입력 : "123".rjust(5,"a")
# 출력 : aa123