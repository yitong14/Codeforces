# 06 - 三角形最小路径和

def f(triangle):
    if len(triangle) == 1:
        return triangle[0][0]
    d = [[triangle[0][0]]]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            d.append([])
            if j == 0:
                d[i].append(d[i-1][j]+triangle[i][j])
            elif j == len(triangle[i]) - 1:
                d[i].append(d[i-1][j-1]+triangle[i][j])
            else:
                d[i].append(min(d[i-1][j-1], d[i-1][j])+triangle[i][j])
    return min(d[len(triangle)-1])


n = int(input())
tri = []
for i in range(n):
    tri.append(list(map(int, input().split())))
print(f(tri))
