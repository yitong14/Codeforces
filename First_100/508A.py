# 508A - pasha and pixels


def check(matrix, x, y):
    if matrix[x][y+1] and matrix[x+1][y+1] and matrix[x+1][y]:
        return True
    if matrix[x][y+1] and matrix[x-1][y+1] and matrix[x-1][y]:
        return True
    if matrix[x][y-1] and matrix[x-1][y-1] and matrix[x-1][y]:
        return True
    if matrix[x][y-1] and matrix[x+1][y-1] and matrix[x+1][y]:
        return True
    return False


n, m, k = map(int, input().split())
colors = [[0]*(m+2) for i in range(n+2)]
for j in range(k):
    x, y = map(int, input().split())
    colors[x][y] = 1
    if check(colors, x, y):
        print(j + 1)
        break
else:
    print(0)
