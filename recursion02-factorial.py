# 02-factorial阶乘

def factorial(n):
    if n in [0, 1]:
        return n
    return n * factorial(n-1)


m = int(input())
print(factorial(m))
