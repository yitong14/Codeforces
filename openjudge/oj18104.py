# 18104 - 饼干分配
kids = [int(s) for s in input().split()]
biscuits = [int(s) for s in input().split()]
kids.sort()
biscuits.sort()
count = 0
i = 0
for k in kids:
    for j in range(i, len(biscuits)):
        if biscuits[j] >= k:
            count += 1
            i = j+1
            break
    else:
        break
print(count)
