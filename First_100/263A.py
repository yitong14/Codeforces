# 263A - beautiful matrix

row = 0
col = 0
for i in range(5):
    s = list(input().split(' '))
    if '1' in s:
        col = s.index('1') + 1
        row = i + 1
step = 0
if row != 3:
    step += abs(row - 3)
if col != 3:
    step += abs(col - 3)
print(step)
