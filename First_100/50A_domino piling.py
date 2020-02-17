# 50A - domino piling
m, n = map(int, input().split())
a = m
b = n // 2
count = a * b
if n % 2 != 0:
    count += m // 2
print(count)
