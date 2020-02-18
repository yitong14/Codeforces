# 16528 - 充实的寒假生活
n = int(input())
schedule = [0]*61
count = 0
activity = [list(map(int, input().split())) for i in range(n)]
activity = sorted(activity, key=lambda x: x[1]-x[0]+1)
for s, e in activity:
    if sum(schedule[s:e+1]) == 0:
        schedule[s:e+1] = [1]*(e-s+1)
        count += 1
print(count)