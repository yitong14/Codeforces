# 584A - olesya and rodion
n, t = map(int, input().split())
multi = max(10**(n-1) // t, 1)
temp = 0
while multi > 0:
    if 10**n > multi * t >= 10**(n-1):
        print(multi * t)
        temp = 1
        break
    if multi * t >= 10**n:
        break
    multi += 1
if temp == 0:
    print(-1)