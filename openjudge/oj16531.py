# 16531 - 上机考试
import math
m, n = map(int, input().split())

pro = [-1]*(n+2)
location = [[-1]+[int(s) for s in input().split()]+[-1] for i in range(m)]
location.insert(0, pro)
location.append(pro)

scores = [[int(s) for s in input().split()] for i in range(m*n)]

count = 0
for i in range(1, m+1):
    for j in range(1, n+1):
        cscr = scores[location[i][j]]
        others = [location[i-1][j], location[i+1][j], location[i][j-1], location[i][j+1]]
        for oth in others:
            if oth!=-1 and scores[oth] == cscr:
                count += 1
                break

score = [sum(row) for row in scores]
cnt = {scr: score.count(scr) for scr in set(score)}
cnt = sorted(cnt.items(), key=lambda x: x[0], reverse=True)
excel = 0
max_ = math.floor(m*n*0.4)
for scr, c in cnt:
    if excel + c > max_:
        break
    excel += c

print(count, excel)
