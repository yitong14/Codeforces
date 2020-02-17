# 231A - team
n = int(input())
count = 0
for i in range(n):
    a, b, c = map(int, input().split())
    s = a + b + c
    if s >= 2:
        count += 1
print(count)