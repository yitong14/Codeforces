# 677A - vanya and fence

n, h = map(int, input().split())
heights = list(map(int, input().split()))
width = 0
for height in heights:
    width += 1
    if height > h:
        width += 1
print(width)

