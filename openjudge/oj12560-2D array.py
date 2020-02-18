# 12560 - 生存游戏

def check(matrix, x, y):
    alive = matrix[x-1][y-1] + matrix[x-1][y] + matrix[x-1][y+1] + \
            matrix[x][y-1] + matrix[x][y+1] + \
            matrix[x+1][y-1] + matrix[x+1][y] + matrix[x+1][y+1]
    if matrix[x][y] and alive == 2:
        return 1
    elif alive == 3:
        return 1
    else:
        return 0


n, m = map(int, input().split())
cells = [[int(c) for c in input().split()] for i in range(n)]
generated = [[0 for i in range(m+2)]]
for i in range(n):
    generated.append([0] + cells[i] + [0])
generated.append(generated[0])
new_cells = [[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        new_cells[i][j] = check(generated, i+1, j+1)
for i in range(n):
    print(' '.join([str(c) for c in new_cells[i]]))

