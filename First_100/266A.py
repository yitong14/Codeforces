# 266A - stones on the table
n = int(input())
color = input()
count = 0
for i, col in enumerate(color):
    if i > 0:
        if col == color[i - 1]:
            count += 1
print(count)
