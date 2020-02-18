# 07 - 1085A - right-left cipher

t = list(input())
length = len(t)
s = []
if length % 2 == 0:
    i = length // 2 - 1
    while i >= 0:
        s.append(t.pop(i))
        s.append(t.pop(i))
        i -= 1
else:
    i = length // 2
    while i >= 1:
        s.append(t.pop(i))
        s.append(t.pop(i))
        i -= 1
    s.append(t.pop(0))
print("".join(s))
