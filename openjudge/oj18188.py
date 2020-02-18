# 18188 - 图像的均值滤波
def mean_graph(matrix, x, y):
    mean_ = [matrix[x-1][y-1], matrix[x-1][y], matrix[x-1][y+1],
             matrix[x][y-1], matrix[x][y], matrix[x][y+1],
             matrix[x+1][y-1], matrix[x+1][y], matrix[x+1][y+1]]
    return int(sum(mean_)/(9-mean_.count(0)))


m, n = map(int, input().split())
pro = [0]*(n+2)
graph = [[0]+[int(s) for s in input().split()]+[0] for i in range(m)]
graph.insert(0, pro)
graph.append(pro)

graph_new = [[0]*n for i in range(m)]
for i in range(1, m+1):
    for j in range(1, n+1):
        graph_new[i-1][j-1] = str(mean_graph(graph, i, j))

for row in graph_new:
    print(' '.join(row))