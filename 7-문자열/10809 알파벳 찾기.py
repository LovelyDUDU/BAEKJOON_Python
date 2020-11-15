word = input()
arr = list(word)

alphabet = list(range(ord('a'), ord('z')+1))

for w in alphabet:
    if chr(w) in arr:
        print(arr.index(chr(w)), end=' ')
    else :
        print(-1, end=' ')


# s = input()
# for i in 'abcdefghijklmnopqrstuvwxyz':
#     try:
#         print(s.index(i),end = ' ')
#     except:
#         print(-1, end = ' ')
# 이런 방법도 있네 ㅋㅋㅋㅋㅋㅋ
