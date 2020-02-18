# 707A - brain's photos
n, m = map(int, input().split())
result = False
matrix = [[s for s in input().split()] for i in range(n)]
for row in matrix:
    if 'C' in row or 'M' in row or 'Y' in row:
        result = True
        break
if result:
    print('#Color')
else:
    print('#Black&White')