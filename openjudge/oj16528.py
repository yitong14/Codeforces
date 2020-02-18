# oj16528 - 充实的寒假生活 - 复习

n = int(input())
dates = {i for i in range(61)}
events = []
for i in range(n):
    s = input()
    a, b = map(int, s.split())
    events.append((b - a, s))
# 天数由小到大排列
events.sort()
count = 0
for days, event in events:
    a, b = map(int, event.split())
    sub_dates = {i for i in range(a, b+1)}
    if sub_dates <= dates:
        dates = dates - sub_dates
        count += 1
print(count)
