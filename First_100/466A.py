# 466A - cheap travel
n, m, a, b = map(int, input().split())
if b / m >= a:
    print(n*a)
else:
    print(min(n//m*b + n%m*a, n//m*b+b))