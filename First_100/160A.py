# 160A - twins

n = int(input())
coins = input().split()
coins_int = [int(n) for n in coins]
coins_int.sort()
coins_int.reverse()
all_coins = sum(coins_int)
take_coins = 0
for i, coin in enumerate(coins_int):
    take_coins += coin
    if take_coins > all_coins - take_coins:
        print(i + 1)
        break
