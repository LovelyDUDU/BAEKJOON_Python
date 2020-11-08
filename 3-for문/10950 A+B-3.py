x = int(input())
list = []
for i in range(0,x):
    a,b = map(int, input().split())
    list.append(a+b)

for i in range(len(list)):
    print(list[i])

# x = int(input())
# for i in range(0,x):
#     a,b = map(int, input().split())
#     print(a+b)

# 백준 문제에서는 5를 입력받으면 5가지의 예시?를 입력받은후 한꺼번에 출력인줄 알았는데
# 그냥 하나 입력받고 하나 출력하는 것을 5번 반복해도 통과되더라....