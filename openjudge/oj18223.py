# 18223 - 24点
def points(a, b, c, d):
    if a+b+c+d == 24:
        return True
    if a+b+c-d == 24:
        return True
    if a+b-c+d == 24:
        return True
    if a-b+c+d == 24:
        return True
    if a+b-c-d == 24:
        return True
    if a-b+c-d == 24:
        return True
    if a-b-c+d == 24:
        return True
    if a-b-c-d == 24:
        return True
    return False


m = int(input())
for i in range(m):
    x1, x2, x3, x4 = map(int, input().split())
    if points(x1, x2, x3, x4):
        print('YES')
        continue
    if points(x2, x1, x3, x4):
        print('YES')
        continue
    if points(x3, x1, x2, x4):
        print('YES')
        continue
    if points(x4, x1, x2, x3):
        print('YES')
        continue
    print('NO')
