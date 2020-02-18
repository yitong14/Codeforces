# 16529 - 股票
n = int(input())
prices = list(map(float, input().split()))
r = 1
min_ = prices[0]
max_ = prices[0]
for i, p in enumerate(prices):
    if p > max_:
        max_ = p
        r = max(r, max_/min_)
    if p < min_:
        min_ = p
        max_ = p
print('{:.2f}'.format(100*r))