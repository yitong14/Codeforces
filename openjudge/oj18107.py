# D - 质数个数 - pass

import math
def is_prime(a):
    if a == 1:
        return False
    divisor = math.floor(a ** 0.5)
    while divisor > 1:
        if a % divisor == 0:
            return False
        divisor -= 1
    return True
t = int(input())
for i in range(t):
    m, n = map(int, input().split())
    prime = []
    for j in range(m, n+1):
        if is_prime(j):
            prime.append(str(j))
    if prime:
        print(' '.join(prime))
    else:
        print(-1)
