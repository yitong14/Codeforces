# F - 因材施教
n, m = map(int, input().split())
levels = [int(s) for s in input().split()]
levels.sort()

total_ = levels[-1] - levels[0]

diff = []
for i in range(n):
    if i == 0:
        continue
    diff.append(levels[i] - levels[i-1])
diff.sort(reverse=True)

print(total_-sum(diff[:m-1]))
