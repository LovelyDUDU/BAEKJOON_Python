all_num = set(range(1, 10001))
not_selfnum = set()

for num in all_num:
    for i in str(num):
        num += int(i)
    not_selfnum.add(num)

answer = all_num - not_selfnum

for a in sorted(answer):
    print(a)

