# 01 - 爬楼梯 - dp
def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return f(n-1) + f(n-2)


n = int(input())
print(f(n))
