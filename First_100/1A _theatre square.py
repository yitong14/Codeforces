n, m, a = map(int, input().split())
x = n / a
y = m / a
if x != n // a:
    x = n // a + 1
if y != m // a:
    y = m // a + 1
print(int(x*y))