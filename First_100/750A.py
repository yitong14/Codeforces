# 03 - 750A - new year and hurry

n, k = map(int, input().split())
total = 0
temp = 0
for i in range(n):
    total += i * 5 + 5
    if total > 240 - k:
        print(i)
        temp = 1
        break
if temp == 0:
    print(n)
