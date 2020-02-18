# 189A - cut ribbon

def find(n, i, j):
    iis = n // i
    for k in range(iis):
        if (n-(iis-k)*i) % j == 0:
            return iis-k, (n-(iis-k)*i) // j
    return False


n, a, b, c = map(int, input().split())
abc = [a, b, c]
abc.sort()
results = []
a, b, c = abc
if n % a == 0:
    results.append(n // a)
elif n % b == 0:
    results.append(n // b)
elif n % c == 0:
    results.append(n // c)

if find(n, a, b):
    aas, bbs = find(n, a, b)
    results.append(aas+bbs)
if find(n, a, c):
    aas, ccs = find(n, a, c)
    results.append(aas+ccs)
if find(n, b, c):
    bbs, ccs = find(n, b, c)
    results.append(ccs+bbs)

for i in range(n//a):
    if find(n-(n//a - i)*a, b, c):
        bbs, ccs, = find(n-(n//a - i)*a, b, c)
        results.append(n//a - i+bbs+ccs)

print(max(results))
