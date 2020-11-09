# import sys
# input = sys.stdin.readline

# while True:
#     A,B = map(int, input().split())
#     if 0<A<10 and 0<B<10:
#         print(A+B)
#     else:
#         break

# 이렇게 풀었다가
# 런타임에러 = 해결못함 만 4번인가 5번ㅋㅋㅋ
# break도 해보고 무한loop도 돌려봤는데 왜 통과를 못하는지 이해 못하다가 
# 1시간 넘어서 걍 구글링했따....정답은 try except 사용.........
# 혹은 입력 받고 안받고로도 할수있는것같더라!

import sys
input = sys.stdin.readline

while True:
    try:
        A,B = map(int, input().split())
        print(A+B)
    except:
        break

# 다른 경우로
# import sys
# for i in sys.stdin:
#     a, b = map(int, i.split())
#     print(a+b)

# 또 다른 경우 (more short coding)
# import sys
# r_input= sys.stdin

# for i in r_input:
# 	print(sum(map(int, i.split())))