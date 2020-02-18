# E - 池塘数目 - pass - 搜索！

def search(matrix, x, y):
    if matrix[x][y+1]:
        matrix[x][y+1] = 0
        matrix = search(matrix, x, y+1)
    if matrix[x][y-1]:
        matrix[x][y-1] = 0
        matrix = search(matrix, x, y-1)
    if matrix[x+1][y]:
        matrix[x+1][y] = 0
        matrix = search(matrix, x+1, y)
    if matrix[x+1][y+1]:
        matrix[x+1][y+1] = 0
        matrix = search(matrix, x+1, y+1)
    if matrix[x+1][y-1]:
        matrix[x+1][y-1] = 0
        matrix = search(matrix, x+1, y-1)
    if matrix[x-1][y+1]:
        matrix[x-1][y+1] = 0
        matrix = search(matrix, x-1, y+1)
    if matrix[x-1][y]:
        matrix[x-1][y] = 0
        matrix = search(matrix, x-1, y)
    if matrix[x-1][y-1]:
        matrix[x-1][y-1] = 0
        matrix = search(matrix, x-1, y-1)
    return matrix


t = int(input())
counts = []
for i in range(t):
    n, m = map(int, input().split())
    pond = [[0]*(m+2)]
    for j in range(n):
        s = input().replace('.', '0')
        pond.append([0]+[int(char) for char in s.replace('W', '1')]+[0])
    pond.append([0]*(m+2))
    count = 0
    for j in range(n):
        for k in range(m):
            if pond[j+1][k+1] == 0:
                continue
            else:
                pond[j+1][k+1] = 0
                pond = search(pond, j+1, k+1)
                count += 1
    counts.append(count)
for c in counts:
    print(c)
