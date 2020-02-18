# D - 二维矩阵上的卷积运算
def multi_matrix(arr1, arr2):
    resul1 = 0
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            resul1 += arr1[i][j] * arr2[i][j]
    return resul1


m, n, p, q = map(int, input().split())
matrix = [[int(s) for s in input().split()] for i in range(m)]
multi = [[int(s) for s in input().split()] for i in range(p)]
resul = []


for a in range(m-p+1):
    re = []
    for b in range(n-q+1):
        c_matrix = [matrix[k][b:b+q] for k in range(a, a+p)]
        re.append(multi_matrix(c_matrix, multi))
    resul.append(re)

for row in resul:
    print(' '.join([str(s) for s in row]))