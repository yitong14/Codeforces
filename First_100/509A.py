# 509A - maximum in table
n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    matrix = [[1 for i in range(n)] for j in range(n)]
    for i in range(n):
        if i == 0:
            continue
        for j in range(n):
            if j == 0:
                continue
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
    print(matrix[n-1][n-1])