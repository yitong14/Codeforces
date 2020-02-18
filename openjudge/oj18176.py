# 18176 - 2050年成绩计算
t = [1] * (10**4+2)
t[0] = 0
t[1] = 0
t[2] = 1
i = 2
for i in range(2, 10**4):
    if t[i] == 1:
        for j in range(i*2, 10**4+1, i):
            t[j] = 0

m, n = map(int, input().split())
for i in range(m):
    scores = [int(s) for s in input().split()]
    total = 0
    for scr in scores:
        if int(scr**0.5)**2 == scr and t[int(scr**0.5)] == 1:
            total += scr
    if total == 0:
        print(0)
    else:
        print('{:.2f}'.format(total/len(scores)))