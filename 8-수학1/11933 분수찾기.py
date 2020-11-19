'''
1/1 - 1/2 2/1 3/1 2/2 1/3 1/4 2/3 3/2 4/1 ...

1 1 /
'''

'''
X = int(input())

line = 1
limit = 0
count = 0
while True:
    limit = ((line * line) + line) / 2
    if limit < X:
        line += 1
    else:
        break

right_num = line

if right_num % 2 != 0:
    while True:
        if X == limit:
            print(str(line+1-right_num) + '/' + str(right_num))
            break
        right_num -= 1
        limit -= 1

else:
    while True:
        if X == limit:
            print(str(line+1-right_num) + '/' + str(right_num))
            break
        right_num -= 1
        limit += 1
개짱난다...  디버깅돌려서 결과는 확실히 나오는데 시간오바....
'''

X = int(input())

line = 1
limit = 0
count = 0
while True:
    limit = ((line * line) + line) / 2
    if limit < X:
        line += 1
    else:
        break

step = int(X - limit)
if step < 0:
    left_num = 1 - step
    right_num = line + step
    if line % 2 != 0:
        print('{}/{}'.format(left_num, right_num))
    else:
        print('{}/{}'.format(right_num, left_num))
else:
    left_num = 1 + step
    right_num = line - step
    if line % 2 != 0:
        print('{}/{}'.format(left_num, right_num))
    else:
        print('{}/{}'.format(right_num, left_num))