# 270A - fancy fence
t = int(input())
results = [True for i in range(t)]
for i in range(t):
    a = int(input())
    if 360 % (180-a) != 0:
        results[i] = False
for r in results:
    if r:
        print('YES')
    else:
        print('NO')