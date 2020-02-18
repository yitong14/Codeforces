# 155A - i love %username%
n = int(input())
scores = list(map(int, input().split()))
count = 0
for i, s in enumerate(scores):
    if i == 0:
        continue
    if s < min(scores[:i]):
        count += 1
    elif s > max(scores[:i]):
        count += 1
print(count)