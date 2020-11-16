eng = input()
arr = list(eng)

abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '22233344455566677778889999'

time = len(arr)
for w in arr:
    time += int(num[abc.index(w)])

print(time)