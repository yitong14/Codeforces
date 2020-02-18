# 119A - epic game
def gcd(x, y):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    return gcd(y, x % y)


a, b, n = map(int, input().split())
i = 0
while n >= 0:
    n = n - gcd(a, n)
    i += 1
    if n < 0:
        print(i % 2)
        break
    n = n - gcd(b, n)
    i += 1
    if n < 0:
        print(i % 2)
        break
