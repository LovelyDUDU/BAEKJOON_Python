# 사칙연산
import math
A,B = map(int, input().split())
print(A+B)
print(A-B)
print(A*B)
print(math.floor(A/B))
print(A%B)

# 파이썬에서 / 와 //의 차이
# / 와 //는 둘다 나눗셈을 의미하지만
# 결과는 / 는 float, //는 int로 나온다
# math.floor 말고 // 쓰는게 메모리를 덜 쓰는것 같다.