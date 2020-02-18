# 12558 - 岛屿周长
n, m = map(int, input().split())

pro = [0]*(m+2)
island = [[0]+[int(s) for s in input().split()]+[0] for i in range(n)]
island.insert(0, pro)
island.append(pro)

surr = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if island[i][j] == 1:
            surr += 4 - (island[i-1][j] + island[i][j-1] + island[i][j+1] + island[i+1][j])

print(surr)
