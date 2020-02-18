# 540A - combination lock - not pass
n = int(input())
origin = [int(s) for s in input()]
need = [int(s) for s in input()]
steps = 0
for i in range(n):
    steps += min(abs(origin[i]-need[i]), 10-abs(origin[i]-need[i]))
print(steps)