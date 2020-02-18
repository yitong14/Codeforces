# 01 - 546A - soldier and banana - 800

k, n, w = map(int, input().split())
x = 0
for i in range(w):
    x = x + (i+1) * k
if x <= n:
    print(0)
else:
    print(x - n)
