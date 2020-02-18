# 711A - bus to udayland
n = int(input())
matrix = [input() for i in range(n)]
temp = 0
for i, row in enumerate(matrix):
    if 'OO' in row:
        temp = 1
        print('YES')
        matrix[i] = matrix[i].replace('OO', '++', 1)
        break
if temp == 0:
    print('NO')
else:
    for row in matrix:
        print(row)
