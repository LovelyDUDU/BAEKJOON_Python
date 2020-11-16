word = input()
word = word.upper()  # 모두 대문자로 변환
arr = list(word)  # list에 담음

dic = {}
for w in arr:
    if w not in dic:  # dictionary 에 없으면 개수를 1로 하고 저장
        dic[w] = 1
    else:  # dictionary에 있으면 기존 개수 + 1
        dic[w] = dic[w] + 1

maxNum = 0
temp = ""
result = ""
for key, value in dic.items():
    if value > maxNum:
        maxNum = value
        temp = ""
        result = key
    elif value == maxNum:
        temp = "?"
        maxNum = value
        result = key

if temp == "?":
    print(temp)
else :
    print(result)


# t=input().upper()
# lt=list(set(t))
#
# countmax=0
# most="?"
#
# for i in lt:
#     if t.count(i)>countmax:
#         countmax=t.count(i)
#         most=i
#     elif t.count(i)==countmax:
#         most="?"
#
# print(most)

#  이런식으로 좀 더 짧게 코딩도 가능하다.
#  나는 dictionary에 값을 담아서 확인했는데
# 이 경우에는 그렇게 안했네.......