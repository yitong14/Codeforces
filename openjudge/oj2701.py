# 2701 - 与7无关的数
relevant = [7, 17, 27, 37, 47, 57, 67,
            70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
            87, 97]
for i in range(7, 100, 7):
    if i not in relevant:
        relevant.append(i)

n = int(input())
cnt = 0
for i in range(1, n+1):
    if i not in relevant:
        cnt += i**2
print(cnt)
