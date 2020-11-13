import sys

input_num = sys.stdin.readline

total = 1
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for _ in range(3):
    total = total * int(input_num())

for i in range(len(str(total))):
    arr[int(str(total)[i])] = arr[int(str(total)[i])] + 1

for i in range(len(arr)):
    print(arr[i])

# a = int(input()) #a,b,c의 값을 입력받음
# b = int(input())
# c = int(input())
#
# num = a*b*c #a,b,c를 곱한 값을 변수 num에 저장
# result=list(str(num)) #num에 저장된 값을 변수 result로 옮겨 리스트화 함
#
# for i in range(10): #숫자 0부터 9까지
#     print(result.count(str(i))) #count()를 이용하여 사용된 숫자를 셈

# 오 이런 방법도 있다. result에 list로 담고 그 안에 해당하는 num의 숫자를 셈...
