# 18211 - 军备竞赛
money = int(input())
prices = [int(s) for s in input().split()]
prices.sort()
k = len(prices) - 1
more = 0
i = 0
while True:
    if money >= prices[i]:
        money -= prices[i]
        more += 1
        i += 1
    elif k > i and prices[k] >= prices[i] and more >= 1:
        money = money + prices[k] - prices[i]
        i += 1
        k -= 1
    else:
        print(more)
        break