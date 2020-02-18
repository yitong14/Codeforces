# 546A - soldier and bananas

k, n, w = map(int, input().split())
need = 0
for i in range(w):
    need += k * (i + 1)
if need <= n:
    print(0)
else:
    print(need - n)
