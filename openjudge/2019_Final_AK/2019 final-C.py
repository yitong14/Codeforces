# C - 图的拉普拉斯矩阵
n, m = map(int, input().split())
d = [[0]*n for i in range(n)]
A = [[0]*n for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    d[a][a] += 1
    d[b][b] += 1
    A[a][b] = 1
    A[b][a] = 1
c = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        c[i][j] = d[i][j] - A[i][j]
for row in c:
    print(' '.join([str(s) for s in row]))