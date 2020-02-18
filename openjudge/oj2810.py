# 2810 - 完美立方
n = int(input())
cubic = [i**3 for i in range(n+1)]
result = []
for b in range(2, n+1):
    for c in range(b, n+1):
        for d in range(c, n+1):
            for a in range(d+1, n+1):
                if cubic[a] == cubic[b]+cubic[c]+cubic[d]:
                    result.append([a, b, c, d])
result.sort(key=lambda x: x[0])
for row in result:
    print('Cube = {}, Triple = ({},{},{})'.format(row[0], row[1], row[2], row[3]))