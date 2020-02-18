# 2713 - 肿瘤面积
n = int(input())
graph = [[int(s) for s in input().split()]for i in range(n)]
cnt = 0
for row in graph:
    if row.count(0) == 2:
        start = row.index(0)
        end = row[start+1:].index(0)
        cnt += end
print(cnt)