import sys
input = sys.stdin.readline
N,X = map(int, input().split())

arr = list(map(int, input().split()))
for i in range(len(arr)):
    if arr[i] < X:
        print(arr[i], end=" ")

# 코드로 봤을땐 N을 입력받고 사용을 안한다 ㅋㅋㅋㅋ

# _, max_num = map(int, input().split())
# nums = list(map(int, input().split()))
# for num in nums:
# 	if (num < max_num) : print(num, end=' ')

# 이 사람도 마찬가지 ㅋㅋㅋㅋ 그냥 split해서 list에 담아버리면 되는걸~