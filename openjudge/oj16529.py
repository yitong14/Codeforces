# oj16529 - 股票 - 复习

n = int(input())
prices = [float(p) for p in input().split()]
money = 100
buy = prices[0]
for i, p in enumerate(prices):
    if p < buy:
        buy = p
        continue
    else:
        current_money = 100 / buy * p
        if current_money > money:
            money = current_money
print(format(money, '.2f'))
