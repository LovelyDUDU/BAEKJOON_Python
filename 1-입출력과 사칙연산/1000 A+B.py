x=input()
A = int(x.split()[0])
B =int(x.split()[1])
print(A+B)


# a,b=map(int,(input().split()))
# print(a+b)

# map(변환함수, 순회 가능한 데이터)
# map()은 여러 개의 데이터를 한 번에 다른 형태로 변환하기 위해서 사용됨
# 보통 list나 tuple을 대상으로 주로 사용함.

# lambda(람다)
# lambda 인자 : 표현식

# 두 수를 더하는 함수
# def hap(x,y):
#   return x+y
# hap(10,20)

# 람다로 표현한 두 수를 더한 함수
# (lambda x,y : x+y)(10,20)