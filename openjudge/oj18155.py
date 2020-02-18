# 18155 - 组合乘积
## my solution
def powerset(nums):
    n = len(nums)

    for i in range(2**n):
        combo = []
        for j in range(n):
            if (i >> j) % 2 == 1:
                combo.append(nums[j])

        yield combo


t = int(input())
s = [int(i) for i in input().split()]
for i in powerset(s):
    find = False
    r = 1
    for d in i:
        r *= d
        if r == t:
            find = True
            break
    if find:
        print('YES')
        break
else:
    print('NO')

## another solution
from functools import reduce
import itertools

t = int(input())
s = list(map(int, input().split()))
m = []
for i in range(1, len(s)+1):
    for j in itertools.combinations(s, i):
        m.append(reduce(lambda x, y: x*y, j))
if t in m:
    print('YES')
else:
    print('NO')