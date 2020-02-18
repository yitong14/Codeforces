# 03-greatest common divisor最大公约数

def gcd(p, q): # 默认p大于q
    if q == 0:
        return p
    return gcd(q, p % q)


m = int(input())
n = int(input())
if m >= n :
    print(gcd(m, n))
else:
    print(gcd(n, m))
