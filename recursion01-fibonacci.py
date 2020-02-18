# 01-fibonacci series
# dynamic programming

'''def fib(n):
    fibs = [0, 1]
    if n in [0, 1]:
        return fibs[:n]
    for i in range(n-2):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


m = int(input())
print(fib(m))
'''

# recursion

def fib(n): # 此种算法与上一种有一个位置的偏差
    if n in [0, 1]:
        return n
    return fib(n-1) + fib(n-2)


m = int(input())
print(fib(m))
