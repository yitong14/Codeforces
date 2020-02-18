# 2750 - 鸡兔同笼
a = int(input())
min_ = a//4
max_ = a//2
result = []
for i in range(min_, max_+1):
    if (a-2*i) % 2 == 0:
        y = (a-2*i) // 2
        x = i - y
        if 2*x + 4*y == a:
            result.append(i)
if len(result) == 0:
    print(0, 0)
else:
    result.sort()
    print(result[0], result[-1])