x,y = map(int, input().split())
time = x*60 + y -45
hour = time//60
min = time%60
if x ==0 and y<45:
    hour = 23
print(hour, min)
