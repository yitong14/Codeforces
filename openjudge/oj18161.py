# 18161 - 矩阵运算
m1, n1 = map(int, input().split())
a = [[int(s) for s in input().split()] for i in range(m1)]
m2, n2 = map(int, input().split())
b = [[int(s) for s in input().split()] for i in range(m2)]
m3, n3 = map(int, input().split())
c = [[int(s) for s in input().split()] for i in range(m3)]
if n1 == m2 and m1 == m3 and n2 == n3:
    new = [[0]*n2 for k in range(m1)]
    for i in range(m1):
        for j in range(n2):
            new[i][j] = str(sum([a[i][k]*b[k][j] for k in range(n1)]) + c[i][j])

    for row in new:
        print(' '.join(row))
else:
    print('Error!')
