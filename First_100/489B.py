# 489B - bersu ball
n = int(input())
boys = list(map(int, input().split()))
m = int(input())
girls = list(map(int, input().split()))
boys.sort()
girls.sort()
match = 0
for b in boys:
    for j, g in enumerate(girls):
        if abs(b-g)<=1:
            match += 1
            del girls[j]
            break
print(match)