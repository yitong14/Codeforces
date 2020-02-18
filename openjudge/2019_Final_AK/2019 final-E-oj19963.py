# E - 买学区房
n = int(input())
distance = [s[1:-1].split(',') for s in input().split()]
prices = [int(s) for s in input().split()]

ratio = []
for dis, p in zip(distance, prices):
    d = int(dis[0]) + int(dis[1])
    ratio.append(d/p)
ratio_rank = sorted(ratio)
prices_rank = sorted(prices)

if len(ratio) == 1:
    median_r = ratio_rank[0]
    median_p = prices_rank[0]
elif len(ratio) % 2 == 0:
    median_r = (ratio_rank[len(ratio)//2] + ratio_rank[len(ratio)//2-1])/2
    median_p = (prices_rank[len(ratio)//2] + prices_rank[len(ratio)//2-1])/2
else:
    median_r = ratio_rank[len(ratio)//2]
    median_p = prices_rank[len(ratio) // 2]

cnt = 0
for r, p in zip(ratio, prices):
    if r > median_r and p < median_p:
        cnt += 1
print(cnt)
