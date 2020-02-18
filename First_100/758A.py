# 758A - holiday of equality
n = int(input())
wealth = list(map(int, input().split()))
if n == 1:
    print(0)
else:
    max_ = max(wealth)
    give = [max_-w for w in wealth]
    print(sum(give))
