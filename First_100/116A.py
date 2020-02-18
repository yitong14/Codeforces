# 116A - tram
n = int(input())
m = 0
current_num = 0
for i in range(n):
    a, b = map(int, input().split())
    current_num += b - a
    if current_num > m:
        m = current_num
print(m)
