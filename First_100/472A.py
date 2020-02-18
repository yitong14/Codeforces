# 06 - 472A - design tutorial: learn from math

def prime(x):
    temp = 1
    if x == 2:
        return temp
    else:
        for i in range(2, x):
            if x % i == 0:
                temp = 0
                break
        return temp


n = int(input())
if n % 2 == 0:
    print(4, n - 4)
else:
    for i in range(4, n):
        if prime(i) == 0 and prime(n - i) == 0:
            print(i, n - i)
            break
