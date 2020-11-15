import sys

input_num = sys.stdin.readline

num = int(input_num())  # 숫자의 개수
num_all = input()  # 숫자N개(공백x)

arr = list(num_all)  # 숫자 N개를 list에 각각 담음

arr = list(map(int, arr))  # 문자로 담긴 arr 리스트를 다 숫자로 바꿔줌
print(sum(arr))  # 합 출력
