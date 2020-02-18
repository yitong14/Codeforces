# 500A - new year transportation

n, t = map(int, input().split())
transportation = {}
adds = list(map(int, input().split()))
for i in range(n-1):
    transportation.update({i+1: adds[i]+i+1})
steps = [1]
while True:
    steps.append(transportation[steps[-1]])
    if steps[-1] >= t:
        break
if t in steps:
    print('YES')
else:
    print('NO')
