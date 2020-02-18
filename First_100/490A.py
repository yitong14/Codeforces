# 490A - team olympiad
n = int(input())
gift = list(map(int, input().split()))
num = min(gift.count(1), gift.count(2), gift.count(3))
print(num)

if num != 0:
    teams = {1: [], 2: [], 3: []}
    for i, g in enumerate(gift):
        teams[g] = teams[g] + [i+1]
    for i in range(num):
        print(teams[1][i], teams[2][i], teams[3][i])