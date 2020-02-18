# 432A - choosing teams
n, k = map(int, input().split())
times = [1 if 5-int(t) >= k else 0 for t in input().split()]
print(sum(times)//3)